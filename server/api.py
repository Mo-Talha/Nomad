import math
import os
import string
import flask
import mongoengine
import redis
import json
import dateutil.parser

import server.colors as colors

from datetime import datetime
from bson import json_util

from models.employer import Employer
from models.job import Job
from models.comment import Comment
from models.rating import AggregateRating

import data.search.elastic as elastic
import analytics.statistics as stats

import shared.secrets as secrets
import shared.logger as logger

COMPONENT = 'API'

app = flask.Flask(__name__, template_folder="./templates")

redis_instance = None

try:
    redis_instance = redis.StrictRedis(host=secrets.REDIS_HOST, port=secrets.REDIS_PORT, db=secrets.REDIS_DB)
except redis.exceptions.ConnectionError:
    redis_instance = None
    pass

try:
    from uwsgidecorators import *
except ImportError:
    def postfork(func):
        pass
    postfork = postfork
    pass


def connect():
    mongoengine.connect(db=secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT, alias='default')


def render_template(*args, **kwargs):
    env = os.environ.get('ENV')

    if not env:
        env = 'dev'

    kwargs.update({
        'env': env
    })
    return flask.render_template(*args, **kwargs)


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def robots():
    return flask.send_from_directory(app.static_folder, flask.request.path[1:])


@app.route("/")
@app.route("/dashboard")
def index():
    return render_template('dashboard.html', page_script='index')


@app.route("/csdashboard")
def cs_dashboard():
    return render_template('dashboard.html', page_script='cs')


@app.route("/jobs")
@app.route("/job")
def display_job():
    employer_name = flask.request.args.get('employer') or ''
    job_title = flask.request.args.get('title') or ''

    employer = Employer.objects(name=employer_name).no_dereference().first()

    job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title, deprecated=False).first()

    if not employer or not job:
        return render_template('404.html')

    summary = job.summary.strip('-').strip('_').strip('-').strip('_').strip().replace('\n', '<br>')\
        .replace('\r\n', '<br>')

    keywords = []

    for keyword in job.keywords:
        color = '#949FB1'

        if keyword.keyword in colors.colors and colors.colors[keyword.keyword]['color']:
            color = colors.colors[keyword.keyword]['color']

        keywords.append({
            'keyword': keyword.keyword,
            'color': color
        })

    job_applicants = 0

    applicants = {}

    if len(applicants) > 0:
        for applicant in job.applicants:
            applicants[applicant.date] = applicant.applicants,

        now = datetime.now()

        earliest = max(date for date in applicants if date < now)

        job_applicants = applicants[earliest][0]

    comments = []

    for comment in job.comments:
        comments.append({
            'comment': comment.comment,
            'date': comment.date.isoformat(),
            'salary': comment.salary,
            'rating': comment.rating.rating * 5,
            'crawled': comment.crawled
        })

    job_data = {
        'employer_name': string.capwords(employer.name),
        'job_id': job.id,
        'job_title': string.capwords(job.title),
        'job_term': job.term,
        'job_year': job.year,
        'job_summary': summary,
        'job_locations': [string.capwords(location.name) for location in job.location],
        'job_openings': job.openings,
        'job_remaining': job.remaining,
        'job_hire_rate': int(job.hire_rate.rating * 100),
        'job_programs': job.programs,
        'job_levels': job.levels,
        'job_keywords': keywords,
        'job_applicants': job_applicants
    }

    return render_template('job.html', job_data=job_data, comments=comments, page_script='job')


@app.route("/jobs/search")
def search_job():
    query = flask.request.args.get('q') or ''
    current_page = flask.request.args.get('p') or 1
    current_page = int(current_page)

    response = elastic.query_jobs(query, current_page)
    time_taken = float(response['took']) / 1000
    total_results = int(response['hits']['total'])

    jobs = []

    if 'hits' in response and 'hits' in response['hits']:
        for job in response['hits']['hits']:
            keywords = []

            for keyword in job['_source']['job_keywords']:
                color = '#949FB1'

                if keyword in colors.colors and colors.colors[keyword]['color']:
                    color = colors.colors[keyword]['color']

                keywords.append({
                    'keyword': keyword,
                    'color': color
                })

            jobs.append({
                'employer_name': string.capwords(job['_source']['employer_name']),
                'job_title': string.capwords(job['_source']['job_title']),
                'job_year': job['_source']['job_year'],
                'job_term': job['_source']['job_term'],
                'job_programs': job['_source']['job_programs'],
                'job_keywords': keywords
            })

    return render_template('job_search.html', jobs=jobs, total_results="{:,}".format(total_results),
                           total_results_unformatted=total_results, page=current_page, query=query,
                           pagination=_get_pagination(current_page, total_results),
                           time_taken=time_taken, page_script='search')


@app.route("/search")
def search():
    query = flask.request.args.get('q') or ''
    current_page = flask.request.args.get('p') or 1
    current_page = int(current_page)

    response = elastic.query_jobs_and_employers(query, current_page)
    time_taken = float(response['took']) / 1000
    total_results = int(response['hits']['total'])

    jobs = []

    if 'hits' in response and 'hits' in response['hits']:
        for job in response['hits']['hits']:
            keywords = []

            for keyword in job['_source']['job_keywords']:
                color = '#949FB1'

                if keyword in colors.colors and colors.colors[keyword]['color']:
                    color = colors.colors[keyword]['color']

                keywords.append({
                    'keyword': keyword,
                    'color': color
                })

            jobs.append({
                'employer_name': string.capwords(job['_source']['employer_name']),
                'job_title': string.capwords(job['_source']['job_title']),
                'job_year': job['_source']['job_year'],
                'job_term': job['_source']['job_term'],
                'job_programs': job['_source']['job_programs'],
                'job_keywords': keywords
            })

    return render_template('search.html', jobs=jobs, total_results="{:,}".format(total_results),
                           total_results_unformatted=total_results, page=current_page, query=query,
                           pagination=_get_pagination(current_page, total_results),
                           time_taken=time_taken, page_script='search')


def _get_pagination(current_page, total_page):
    start_page = current_page - 5
    end_page = current_page + 4
    total_page = int(math.ceil(float(total_page) / 10))

    if start_page <= 0:
        end_page -= (start_page - 1)
        start_page = 1

    if end_page > total_page:
        end_page = total_page
        if end_page > 10:
            start_page = end_page - 9

    return range(start_page, end_page + 1)


@app.route('/api/jobs-vs-programs-stat', methods=['POST'])
def jobs_vs_programs_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsprograms')

    if redis_instance:
        if redis_instance.exists(redis_key):
            programs_vs_jobs = json.loads(redis_instance.get(redis_key))

        else:
            programs_vs_jobs = list(stats.get_jobs_vs_programs())

            redis_instance.set(redis_key, json.dumps(programs_vs_jobs))
            redis_instance.expire(redis_key, 21600)
    else:
        programs_vs_jobs = list(stats.get_jobs_vs_programs())

    response = {
        'data': [{'name': program['_id']['program'], 'jobs': program['count']} for program in programs_vs_jobs]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-levels-stat', methods=['POST'])
def jobs_vs_levels_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvslevels')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_levels = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_levels = list(stats.get_jobs_vs_levels())

            redis_instance.set(redis_key, json.dumps(jobs_vs_levels))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_levels = list(stats.get_jobs_vs_levels())

    response = {
        'data': [{'name': level['_id']['level'], 'jobs': level['count']} for level in jobs_vs_levels]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-terms-stat', methods=['POST'])
def jobs_vs_terms_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsterms')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_terms = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_terms = list(stats.get_jobs_vs_terms())

            redis_instance.set(redis_key, json.dumps(jobs_vs_terms))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_terms = list(stats.get_jobs_vs_terms())

    response = {
        'data': [{'year': term['_id']['year'], 'term': term['_id']['term'], 'jobs': term['count']}
                 for term in jobs_vs_terms]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-locations-stat', methods=['POST'])
def jobs_vs_locations_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvslocations')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_locations = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_locations = list(stats.get_jobs_vs_locations())

            redis_instance.set(redis_key, json.dumps(jobs_vs_locations))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_locations = list(stats.get_jobs_vs_locations())

    response = {
        'data': [{'name': location['_id']['location'], 'longitude': location['_id']['longitude'],
                  'latitude': location['_id']['latitude']} for location in jobs_vs_locations
                 if location['_id']['longitude'] != 0 and location['_id']['latitude'] != 0]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-programming-languages-stat', methods=['POST'])
def jobs_vs_programming_languages_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsprogramminglanguages')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_programming_languages = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_programming_languages = list(stats.get_jobs_vs_programming_languages())

            redis_instance.set(redis_key, json.dumps(jobs_vs_programming_languages))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_programming_languages = list(stats.get_jobs_vs_programming_languages())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_programming_languages]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-databases-stat', methods=['POST'])
def jobs_vs_databases_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsdatabases')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_databases = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_databases = list(stats.get_jobs_vs_databases())

            redis_instance.set(redis_key, json.dumps(jobs_vs_databases))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_databases = list(stats.get_jobs_vs_databases())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_databases]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-operating-systems-stat', methods=['POST'])
def jobs_vs_os_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsos')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_os = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_os = list(stats.get_jobs_vs_operating_systems())

            redis_instance.set(redis_key, json.dumps(jobs_vs_os))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_os = list(stats.get_jobs_vs_operating_systems())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_os]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-web-frameworks-stat', methods=['POST'])
def jobs_vs_web_frameworks_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvswebframeworks')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_web_frameworks = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_web_frameworks = list(stats.get_jobs_vs_web_frameworks())

            redis_instance.set(redis_key, json.dumps(jobs_vs_web_frameworks))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_web_frameworks = list(stats.get_jobs_vs_web_frameworks())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_web_frameworks]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-apache-frameworks-stat', methods=['POST'])
def jobs_vs_apache_frameworks_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsapacheframeworks')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_apache_frameworks = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_apache_frameworks = list(stats.get_jobs_vs_apache_frameworks())

            redis_instance.set(redis_key, json.dumps(jobs_vs_apache_frameworks))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_apache_frameworks = list(stats.get_jobs_vs_apache_frameworks())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_apache_frameworks]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-search-servers-stat', methods=['POST'])
def jobs_vs_search_servers_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvssearchservers')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_search_servers = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_search_servers = list(stats.get_jobs_vs_search_servers())

            redis_instance.set(redis_key, json.dumps(jobs_vs_search_servers))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_search_servers = list(stats.get_jobs_vs_search_servers())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_search_servers]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-js-libraries-stat', methods=['POST'])
def jobs_vs_js_libraries_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvsjslibraries')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_js_libraries = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_js_libraries = list(stats.get_jobs_vs_javascript_libraries())

            redis_instance.set(redis_key, json.dumps(jobs_vs_js_libraries))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_js_libraries = list(stats.get_jobs_vs_javascript_libraries())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_js_libraries]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-css-frameworks-stat', methods=['POST'])
def jobs_vs_css_frameworks_stat():
    redis_key = '{}.{}.stat'.format(COMPONENT, 'jobsvscsslibraries')

    if redis_instance:
        if redis_instance.exists(redis_key):
            jobs_vs_css_frameworks = json.loads(redis_instance.get(redis_key))

        else:
            jobs_vs_css_frameworks = list(stats.get_jobs_vs_css_frameworks())

            redis_instance.set(redis_key, json.dumps(jobs_vs_css_frameworks))
            redis_instance.expire(redis_key, 21600)
    else:
        jobs_vs_css_frameworks = list(stats.get_jobs_vs_css_frameworks())

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_css_frameworks]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/comment', defaults={'job_id': None})
@app.route('/api/comment/<string:job_id>', methods=['POST', 'PUT'])
def comment(job_id):
    data = json.loads(flask.request.data)

    comment_text = data['text']
    comment_date = dateutil.parser.parse(data['date'])
    salary = data['salary'] or 0
    rating = (float(data['rating']) / 5) or 0

    if job_id is not None and comment_text:
        job = Job.objects(id=job_id).first()

        if not job:
            return render_template('404.html')

        logger.info(COMPONENT, 'Adding comment for job: {}'.format(job_id))

        new_comment = Comment(comment=comment_text, date=comment_date, salary=salary, crawled=False,
                              rating=AggregateRating(rating=rating, count=1))

        job.update(push__comments=new_comment)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@postfork
def connect_uwsgi_mongo():
    connect()


if __name__ == "__main__":
    connect()
    app.run(host='0.0.0.0', debug=True)

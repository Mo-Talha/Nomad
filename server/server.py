import os
import string
import flask
import mongoengine
import elasticsearch

from bson import json_util

import analytics.statistics as stats

import shared.secrets as secrets


component = 'API'

app = flask.Flask(__name__, template_folder="./templates")

elastic = elasticsearch.Elasticsearch()


def render_template(*args, **kwargs):
    kwargs.update({
        'env': os.environ.get('ENV') or ''
    })
    return flask.render_template(*args, **kwargs)


def connect():
    mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)


@app.route("/")
@app.route("/dashboard")
def index():
    return render_template('dashboard.html', page_script='index.js')


@app.route("/csdashboard")
def cs_dashboard():
    return render_template('dashboard.html', page_script='cs.js')


@app.route("/search")
def search():
    print flask.request.args.get('q')
    response = elastic.search(index='jobmine', doc_type=['jobs'], body={
        "from": 0, "size": 15,
        "query": {
            "multi_match": {
                "query": flask.request.args.get('q'),
                "type": "cross_fields",
                "fields": ["employer_name^4", "job_title^4", "job_term"]
            },

        }
    })

    jobs = []

    if 'hits' in response and 'hits' in response['hits']:
        for job in response['hits']['hits']:
            jobs.append({
                'employer_name': string.capwords(job['_source']['employer_name']),
                'job_title': string.capwords(job['_source']['job_title']),
                'job_year': job['_source']['job_year'],
                'job_term': job['_source']['job_term'],
                'job_programs': job['_source']['job_programs'],
                'job_keywords': job['_source']['job_keywords']
            })

    return render_template('search.html', jobs=jobs, total_results="{:,}".format(int(response['hits']['total'])),
                           time_taken=float(response['took']) / 1000)


@app.route('/api/jobs-vs-programs-stat', methods=['POST'])
def jobs_vs_programs_stat():
    programs_vs_jobs = stats.get_jobs_vs_programs()

    response = {
        'data': [{'name': program['_id']['program'], 'jobs': program['count']} for program in programs_vs_jobs]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-levels-stat', methods=['POST'])
def jobs_vs_levels_stat():
    jobs_vs_levels = stats.get_jobs_vs_levels()

    response = {
        'data': [{'name': level['_id']['level'], 'jobs': level['count']} for level in jobs_vs_levels]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-terms-stat', methods=['POST'])
def jobs_vs_terms_stat():
    jobs_vs_terms = stats.get_jobs_vs_terms()

    response = {
        'data': [{'year': term['_id']['year'], 'term': term['_id']['term'], 'jobs': term['count']}
                 for term in jobs_vs_terms]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-locations-stat', methods=['POST'])
def jobs_vs_locations_stat():
    jobs_vs_locations = stats.get_jobs_vs_locations()

    response = {
        'data': [{'name': location['_id']['location'], 'longitude': location['_id']['longitude'],
                  'latitude': location['_id']['latitude']} for location in jobs_vs_locations
                 if location['_id']['longitude'] != 0 and location['_id']['latitude'] != 0]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-programming-languages-stat', methods=['POST'])
def jobs_vs_programming_languages_stat():
    jobs_vs_programming_languages = stats.get_jobs_vs_programming_languages()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_programming_languages]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-databases-stat', methods=['POST'])
def jobs_vs_databases_stat():
    jobs_vs_databases = stats.get_jobs_vs_databases()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_databases]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-operating-systems-stat', methods=['POST'])
def jobs_vs_os_stat():
    jobs_vs_os = stats.get_jobs_vs_operating_systems()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_os]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-web-frameworks-stat', methods=['POST'])
def jobs_vs_web_frameworks_stat():
    jobs_vs_web_frameworks = stats.get_jobs_vs_web_frameworks()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_web_frameworks]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-apache-frameworks-stat', methods=['POST'])
def jobs_vs_apache_frameworks_stat():
    jobs_vs_apache_frameworks = stats.get_jobs_vs_apache_frameworks()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_apache_frameworks]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-search-servers-stat', methods=['POST'])
def jobs_vs_search_servers_stat():
    jobs_vs_search_servers = stats.get_jobs_vs_search_servers()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_search_servers]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-js-libraries-stat', methods=['POST'])
def jobs_vs_js_libraries_stat():
    jobs_vs_js_libraries = stats.get_jobs_vs_javascript_libraries()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_js_libraries]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-css-frameworks-stat', methods=['POST'])
def jobs_vs_css_frameworks_stat():
    jobs_vs_css_frameworks = stats.get_jobs_vs_css_frameworks()

    response = {
        'data': [{'name': language['_id']['keyword'], 'jobs': language['count']}
                 for language in jobs_vs_css_frameworks]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


if __name__ == "__main__":
    connect()
    app.run(host='0.0.0.0', debug=True)

import os
import flask
import mongoengine

from bson import json_util

import analytics.statistics as stats
import shared.secrets as secrets


app = flask.Flask(__name__, template_folder="./templates")


def render_template(*args, **kwargs):
    kwargs.update({
        'env': os.environ.get('ENV') or ''
    })
    return flask.render_template(*args, **kwargs)


@app.route("/")
def index():
    return render_template('index.html', page_script='index.js')


@app.route('/api/programs-vs-jobs-stat', methods=['POST'])
def programs_vs_jobs_stat():
    programs_vs_jobs = stats.get_programs_vs_jobs()

    response = {
        'data': [{'name': program, 'jobs': programs_vs_jobs[program]} for program in programs_vs_jobs]
    }

    return flask.Response(response=json_util.dumps(response), status=200, mimetype="application/json")


@app.route('/api/jobs-vs-levels-stat', methods=['POST'])
def jobs_vs_levels_stat():
    jobs_vs_levels = stats.get_jobs_vs_levels()

    response = {
        'data': [{'name': level, 'jobs': jobs_vs_levels[level]} for level in jobs_vs_levels]
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


if __name__ == "__main__":
    mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)
    app.run(host='0.0.0.0', debug=True)

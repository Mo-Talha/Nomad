import os
import flask


app = flask.Flask(__name__, template_folder="./templates")


def render_template(*args, **kwargs):
    kwargs.update({
        'env': os.environ.get('ENV') or ''
    })
    return flask.render_template(*args, **kwargs)


@app.route("/")
def index():
    return render_template('index.html', page_script='index.js')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

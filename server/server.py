import flask


app = flask.Flask(__name__, template_folder="./templates", static_folder="./static/dist")


@app.route("/")
def hello():
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

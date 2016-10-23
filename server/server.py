import mongoengine

import shared.secrets as secrets

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


def before_app():
    mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

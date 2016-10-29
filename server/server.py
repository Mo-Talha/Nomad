import flask


app = flask.Flask(__name__, template_folder="./templates", static_folder="./static/")


def render_template(*args, **kwargs):
    redis = view_helpers.get_redis_instance()

    current_user = view_helpers.get_current_user()
    should_renew_fb_token = False
    if (current_user and
        current_user.fbid and
        not current_user.is_demo_account and
        not hasattr(flask.request, 'as_user_override')):
        should_renew_fb_token = current_user.should_renew_fb_token

    kwargs.update({
        'env': app.config['ENV'],
        'VERSION': VERSION,
        'NUM_KITTENS': len(KITTEN_DATA),
        'js_dir': app.config['JS_DIR'],
        'ga_property_id': app.config['GA_PROPERTY_ID'],
        'total_points': int(redis.get('total_points') or 0),
        'current_user': current_user,
        'should_renew_fb_token': should_renew_fb_token,
        'current_term_id': util.get_current_term_id(),
    })
    return render_template(*args, **kwargs)

@app.route("/")
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

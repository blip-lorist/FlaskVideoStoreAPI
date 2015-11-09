# @app.route("/")
# def hello():
#     return "Hello World!"
#
# # Be sure to use trailing slashes
# @app.route("/unigoats/")
# def whatever():
#     return "this is another page"

from video_store import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

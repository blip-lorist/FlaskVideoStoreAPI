from video_store import app

@app.route('/')
@app.route('/index')
def index():
    return "Video Store API!"

@app.route('/')
@app.route('/customers/')
def customers():
    return "List of customers!"

@app.route('/')
@app.route('/customers/<int:id>')
def customer(id):
    return "A customer's profile!"

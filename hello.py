from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Be sure to use trailing slashes
@app.route("/unigoats/")
def whatever():
    return "this is another page"

if __name__ == "__main__":
    app.run(debug=True)

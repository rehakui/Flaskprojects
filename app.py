from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/about")
def about():
    return "About"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

app.run(debug=True)
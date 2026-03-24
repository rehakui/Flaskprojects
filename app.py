from flask import Flask, request

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

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    return {"you_sent": data}

@app.route("/search")
def search():
    keyword = request.args.get("q")
    return f"search: {keyword}"

app.run(debug=True)
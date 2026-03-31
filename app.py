from flask import Flask, request, render_template

app = Flask(__name__)

users = []
next_id = 1

# 取得
@app.route("/users", methods=["GET"])
def get_users():
    return users

# 追加
@app.route("/users", methods=["POST"])
def add_user():
    global next_id
    data = request.json
    user = {
        "id": next_id,
        "name": data["name"]
    }
    users.append(user)
    next_id += 1

    return user, 201

# 削除
@app.route("/users/<int:index>", methods=["DELETE"])
def delete_user(index):
    if index < len(users):
        deleted = users.pop(index)
        return deleted
    return {"error": "not found"}, 404

# 更新
@app.route("/users/<int:index>", methods=["PUT"])
def update_user(index):
    if index < len(users):
        data = request.json
        users[index]["name"] = data["name"]
        return users[index]
    return {"error": "not found"}, 404

@app.route("/")
def home():
    return "Home"

@app.route("/about")
def about():
    return "About"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

# API(JSON) curlにてlogin
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     return {"you_sent": data}

# Webページ(HTML) htmlフォームにてlogin
@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    return (f"<h1>Hello {name}.<br>"
            f"Nice to meet you.</h1>")


@app.route("/search")
def search():
    keyword = request.args.get("q")
    return f"search: {keyword}"

@app.route("/status")
def status():
    return {"status": "ok"}, 200

@app.route("/error")
def notfound():
    return {"error": "something wrong"}, 500

app.run(debug=True)
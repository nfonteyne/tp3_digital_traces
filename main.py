from flask import render_template, redirect, url_for, Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("main.html")
@app.route("/<name>")
def user(name):
    return f"Hello-- {name}!"
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
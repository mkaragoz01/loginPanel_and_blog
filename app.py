from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/blog")
def blogPage():
    return render_template("kişisel_blog.html")

if __name__ == "__main__":
    app.run(debug=True)
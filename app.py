from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/blog")
def blogPage():
    # Kullanıcı için veritabanı bağlantısı
    """
    baglanti = sqlite3.connect("/database/user_control.db")
    isaretci = baglanti.cursor(f"select * from user_control where pw=''")
    users = isaretci.fetchall()
    baglanti.commit()
    baglanti.close()
    """
    return render_template("kişisel_blog.html")

if __name__ == "__main__":
    app.run(debug=True)
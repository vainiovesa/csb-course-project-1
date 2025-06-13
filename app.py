from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password_1 = request.form["password-1"]
        password_2 = request.form["password-2"]
        if password_1 != password_2:
            return redirect("/register")

        sql = f"INSERT INTO Users (username, password) VALUES ('{username}', '{password_1}')"
        db_execute(sql)

        return redirect("/")

    return render_template("register.html")

def db_execute(sql):
    con = sqlite3.connect("database.db")
    con.execute(sql)
    con.commit()
    con.close()

if __name__=="__main__":
    app.run(debug=True)

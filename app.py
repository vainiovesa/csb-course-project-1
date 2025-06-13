from flask import Flask, render_template, redirect, session, request
import sqlite3
import config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = f"SELECT id, password FROM Users WHERE username = '{username}'"
        user_id, actual_password = db_query(sql)[0]
        if not actual_password:
            return redirect("/login")
        if password != actual_password:
            return redirect("/login")

        session["user_id"] = user_id

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

def db_query(sql):
    con = sqlite3.connect("database.db")
    result = con.execute(sql).fetchall()
    con.close()
    return result

if __name__=="__main__":
    app.run(debug=True)

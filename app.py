from flask import Flask, render_template, redirect, flash, session, request
from string import ascii_letters, digits, punctuation
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
        sql = f"SELECT id, password FROM Users WHERE username = ?"
        user = db_query(sql, [username])
        if not user:
            flash(f"No user with name {username}")
            return redirect("/login")

        user_id, actual_password = user[0]
        if password != actual_password:
            flash(f"Incorrect password")
            return redirect("/login")

        session["user_id"] = user_id
        flash(f"Logged in as {username}")

        return redirect("/")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 4:
            flash("Username must be at least 4 characters")
            return redirect("/register")

        password_1 = request.form["password-1"]
        password_2 = request.form["password-2"]
        if password_1 != password_2:
            flash("Passwords don't match")
            return redirect("/register")

        if len(password_1) < 8:
            flash("Password must be at least 8 characters")
            return redirect("/register")

        if password_1 == username:
            flash("Username and password cannot match")
            return redirect("/register")

        if not any([ltr in password_1 for ltr in ascii_letters]):
            flash("Password must include letters")
            return redirect("/register")

        if not any([num in password_1 for num in digits]):
            flash("Password must include numbers")
            return redirect("/register")
        
        if not any([num in password_1 for num in punctuation]):
            flash(f"Password must include punctuation characters ({punctuation})")
            return redirect("/register")

        sql = f"INSERT INTO Users (username, password) VALUES (?, ?)"
        db_execute(sql, [username, password_1])

        flash(f"Account {username} created")
        return redirect("/")

    return render_template("register.html")

def db_execute(sql, params=[]):
    con = sqlite3.connect("database.db")
    con.execute(sql, params)
    con.commit()
    con.close()

def db_query(sql, params=[]):
    con = sqlite3.connect("database.db")
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

if __name__=="__main__":
    app.run(debug=True)

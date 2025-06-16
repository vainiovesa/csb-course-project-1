### Overview
Course Project I for the course series Cyber Security Base 2025 (University of Helsinki). This project is a web application that has 5 different flaws from the OWASP 2017
[top ten list](https://owasp.org/www-project-top-ten/2017/Top_10) and their fixes. The application will be built with Python using Flask.

### Installing and running the application
First, copy this Github project to your machine. You will then have to run the following commands in the project directory.

Make a virtual environment (if you do not have Flask installed).
```console
$ python3 -m venv venv
```
Activate the virtual environment.
```console
$ source venv/bin/activate
```
Install Flask.
```console
$ pip3 install flask
```
Create a database.
```console
$ sqlite3 database.db < schema.sql
```
Run the application.
```console
$ python3 app.py
```


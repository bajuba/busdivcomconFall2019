from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
from database import Admins, app

## https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp
## use this to find bootstrap classes

username = ""
error_message = ""

@app.route("/", methods = ["post"])
def verify():
    global username
    global error_message

    username = request.form["username"]
    password = request.form["password"]

    current_user = Admins.query.filter_by(username = username).first()

    if(current_user):
        if(check_password_hash(current_user.password, password)):
            return render_template("admin_dashboard.html")
        else:
            error_message = "Your username and/or password combination could not be found within our database."
            return redirect(url_for("index"))
    else:
        error_message = "Your username and/or password combination could not be found within our database."
        return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("admin_login.html", username = username, error_message = error_message)

app.run()
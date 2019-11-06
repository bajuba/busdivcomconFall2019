from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from database import app, Admins
import admin_dashboard
import admin_contests
import admin_events
import admin_pictures
import admin_schools
import admin_students
import admin_teachers

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
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            error_message = "Your username and/or password combination could not be found within our database."
            return redirect(url_for("admin_login"))
    else:
        error_message = "Your username and/or password combination could not be found within our database."
        return redirect(url_for("admin_login"))

@app.route("/admin_logout")
def admin_logout():
    global username
    global error_message

    username = ""
    error_message = ""
    session["admin"] = False

    return redirect(url_for("admin_login"))

@app.route("/")
def admin_login():
    global username
    global error_message

    session["admin"] = False
    
    return render_template("admin_login.html", username = username, error_message = error_message)

app.run()
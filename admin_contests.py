from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Contests, Admins

@app.route("/contests")
def admin_contests():
    if(session["admin"] == True):
        return render_template("admin_contests.html")
    else:
        return redirect(url_for("login"))

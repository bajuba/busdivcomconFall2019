from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Teachers, Admins

@app.route("/teachers")
def admin_teachers():
    if(session["admin"] == True):
        return render_template("admin_teachers.html")
    else:
        return redirect(url_for("login"))

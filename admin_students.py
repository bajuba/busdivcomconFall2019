from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Students, Admins

@app.route("/students")
def admin_students():
    if(session["admin"] == True):
        return render_template("admin_students.html")
    else:
        return redirect(url_for("login"))
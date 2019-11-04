from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Schools, Admins

@app.route("/schools")
def admin_schools():
    if(session["admin"] == True):
        return render_template("admin_schools.html")
    else:
        return redirect(url_for["login"])
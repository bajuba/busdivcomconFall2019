from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Pictures, Admins

@app.route("/admin_pictures")
def admin_pictures():
    if(session["admin"] == True):
        return render_template("admin_pictures.html")
    else:
        return redirect(url_for("admin_login"))
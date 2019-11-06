from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Events, Admins

@app.route("/admin_events")
def admin_events():
    if(session["admin"] == True):
        return render_template("admin_events.html")
    else:
        return redirect(url_for("admin_login"))

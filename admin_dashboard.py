from flask import Flask, render_template, request, redirect, url_for, session
from database import *

@app.route("/admin_dashboard")
def admin_dashboard():
    if(session["admin"] == True):
        return render_template("admin_dashboard.html")
    else:
        return redirect(url_for("admin_login"))
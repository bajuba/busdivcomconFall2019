from flask import Flask, render_template, request, redirect, url_for
from database import *

@app.route("/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

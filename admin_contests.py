from flask import Flask, render_template, request, redirect, url_for
from database import app, Contests

@app.route("/contests")
def admin_contests():
    return render_template("admin_contests.html")

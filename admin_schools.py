from flask import Flask, render_template, request, redirect, url_for
from database import app, Schools

@app.route("/schools")
def admin_schools():
    return render_template("admin_schools.html")

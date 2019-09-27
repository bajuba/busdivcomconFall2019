from flask import Flask, render_template, request, redirect, url_for
from database import app, Teachers

@app.route("/teachers")
def admin_teachers():
    return render_template("admin_teachers.html")

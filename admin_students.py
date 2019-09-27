from flask import Flask, render_template, request, redirect, url_for
from database import app, Students

@app.route("/students")
def admin_students():
    return render_template("admin_students.html")

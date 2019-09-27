from flask import Flask, render_template, request, redirect, url_for
from database import app, Pictures

@app.route("/pictures")
def admin_pictures():
    return render_template("admin_pictures.html")

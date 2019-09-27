from flask import Flask, render_template, request, redirect, url_for
from database import app, Events

@app.route("/events")
def admin_events():
    return render_template("admin_events.html")

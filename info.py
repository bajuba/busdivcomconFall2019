from flask import Flask, render_template, request, redirect, url_for
from database import app, Teachers

@app.route('/info')
def info():
  return render_template('info.html')

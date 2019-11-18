from flask import Flask, render_template, request, redirect, url_for
from database import app, Teachers

@app.route('/photos')
def photos():
  return render_template('photos.html')
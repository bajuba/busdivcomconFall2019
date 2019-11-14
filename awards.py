from flask import Flask, render_template, request, redirect, url_for
from database import app, Teachers

@app.route('/awards')
def awards():
  return render_template('awards.html')
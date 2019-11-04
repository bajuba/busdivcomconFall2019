from flask import Flask, request, redirect, render_template
import awards
import photos
import info
app = Flask('app')

@app.route('/')
def index():
  return render_template('home.html')

app.run(host='0.0.0.0', port=8080)
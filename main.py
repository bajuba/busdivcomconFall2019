from flask import Flask, request, redirect, render_template
app = Flask('app')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/info')
def info():
  return render_template('info.html')

@app.route('/photos')
def photos():
  return render_template('photos.html')

@app.route('/awards')
def awards():
  return render_template('awards.html')

app.run(host='0.0.0.0', port=8080)
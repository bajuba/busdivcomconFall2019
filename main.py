from flask import Flask, request, redirect, render_template
app = Flask('app')

@app.route('/')
def index():
  return render_template('base.html')

app.run(host='0.0.0.0', port=8080)
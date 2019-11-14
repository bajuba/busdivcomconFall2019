from flask import Flask, request, redirect, render_template
from database import *
import admin_login
import awards
import photos
import info

@app.route('/')
def index():
  return render_template('home.html')

app.run()

from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Contests, Admins

def contest_query():
    return Contests.query.first()

@app.route("/admin_contests", methods = ["post"])
def update_contest():
    updated_contest_name = form.request["contest_name"]
    updated_contest_date = form.request["contest_date"]
    updated_app_start_date = form.request["app_start_date"]
    updated_app_close_date = form.request["app_closed_date"]
    updated_max_students = form.request["max_students"]
    updated_coord_name = form.request["coord_name"]
    updated_coord_email = form.request["coord_email"]
    updated_coord_phone = form.request["coord_phone"]
    updated_coord_title = form.request["coord_title"]
    updated_dev_name = form.request["dev_name"]
    updated_dev_title = form.request["dev_title"]
    updated_dev_email = form.request["dev_email"]

    contest = contest_query()

    contest.name = updated_contest_name
    contest.contest_date = updated_contest_date
    contest.app_start_date = updated_app_start_date
    contest.app_closed_date = updated_app_close_date
    contest.max_students = updated_max_students
    contest.coord_name = updated_coord_name
    contest.coord_email = updated_coord_email
    contest.coord_phone = updated_coord_phone
    contest.coord_title = updated_coord_title
    contest.dev_name = updated_dev_name
    contest.dev_title = updated_dev_title
    contest.dev_email = updated_dev_title

@app.route("/admin_contests")
def admin_contests():
    if(session["admin"] == True):
        return render_template("admin_contests.html", contest_query = contest_query())
    else:
        return redirect(url_for("admin_login"))

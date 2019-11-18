from flask import Flask, render_template, request, redirect, url_for, session
from database import app, Contests, Admins, db

def query_all_contests():
    return Contests.query.all()

def query_contests_by_id(selected_contest):
    return Contests.query.filter_by()

@app.route("/admin_contests", methods = ["post"])
def update_contest():
    updated_contest_name = request.form["contest_name"]
    updated_contest_date = request.form["contest_date"]
    updated_app_start_date = request.form["app_start_date"]
    updated_app_close_date = request.form["app_closed_date"]
    updated_student_start_date = request.form["student_start_date"]
    updated_student_end_date = request.form["student_end_date"]
    updated_max_students = request.form["max_students"]
    updated_coord_name = request.form["coord_name"]
    updated_coord_email = request.form["coord_email"]
    updated_coord_phone = request.form["coord_phone"]
    updated_coord_title = request.form["coord_title"]
    updated_dev_name = request.form["dev_name"]
    updated_dev_title = request.form["dev_title"]
    updated_dev_email = request.form["dev_email"]

    contest.name = updated_contest_name
    contest.contest_date = updated_contest_date
    contest.app_start_date = updated_app_start_date
    contest.app_closed_date = updated_app_close_date
    contest.student_start_date = updated_app_start_date
    contest.student_end_date = updated_app_close_date
    contest.max_students = updated_max_students
    contest.coord_name = updated_coord_name
    contest.coord_email = updated_coord_email
    contest.coord_phone = updated_coord_phone
    contest.coord_title = updated_coord_title
    contest.dev_name = updated_dev_name
    contest.dev_title = updated_dev_title
    contest.dev_email = updated_dev_email

    ##Create an alert box to notify admin the table has been changed
    ##use Modal Bootstrap

    db.session.commit()

    return redirect(url_for("admin_contests"))

@app.route("/admin_contests")
def admin_contests():
    if(session["admin"] == True):
        query_all_contests = query_all_contests()

        selected_contest = request.form["contest_list"]
        selected_contest = query_contests_by_id(selected_contest)


        return render_template("admin_contests.html", query_all_contests = query_all_contests())
    else:
        return redirect(url_for("admin_login"))

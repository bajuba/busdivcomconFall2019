from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/businessContest'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

app.secret_key = "business_division"

#visit here for examples: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
#example: posts = db.relationship('Post', backref='author', lazy='dynamic')

class Contests(db.Model):
    __tablename__ = "contests"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False, default = "")
    contest_date = db.Column(db.String(255))
    app_start_date = db.Column(db.String(255))
    app_close_date = db.Column(db.String(255))
    student_start_date = db.Column(db.String(255))
    student_end_date = db.Column(db.String(255))
    start_time = db.Column(db.Integer, nullable = False, default = "")
    end_time = db.Column(db.Integer, nullable = False, default = "")
    max_students = db.Column(db.Integer, nullable = False, default = "")
    coord_name = db.Column(db.String(255), nullable = False, default = "")
    coord_email = db.Column(db.String(255), nullable = False, default = "")
    coord_phone = db.Column(db.String(100), nullable = False, default = "")
    coord_title = db.Column(db.String(255), nullable = False, default = "")
    dev_name = db.Column(db.String(255), nullable = False, default = "")
    dev_title = db.Column(db.String(255), nullable = False, default = "")
    dev_email = db.Column(db.String(255), nullable = False, default = "")
    events = db.relationship("Events", backref = "event", lazy = "dynamic")
    schools = db.relationship("Schools", backref = "school", lazy = "dynamic")
    pictures = db.relationship("Pictures", backref = "picture", lazy = "dynamic")

    def __init__(self, name, contest_date, app_start_date, app_close_date, student_start_date, student_end_date, start_time, end_time, max_students, coord_name, coord_email, coord_phone, coord_title, dev_name, dev_title, dev_email):
        self.name = name
        self.contest_date = contest_date
        self.app_start_date = app_start_date
        self.app_close_date = app_close_date
        self.student_start_date = student_start_date
        self.student_end_date = student_end_date
        self.start_time = start_time
        self.end_time = end_time
        self.max_students = max_students
        self.coord_name = coord_name
        self.coord_email = coord_email
        self.coord_phone = coord_phone
        self.coord_title = coord_title
        self.dev_name = dev_name
        self.dev_title = dev_title
        self.dev_email = dev_email

class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False, default = "")
    seat_limit = db.Column(db.Integer, nullable = False, default = "")
    room = db.Column(db.String(255), nullable = False, default = "")
    description = db.Column(db.String(255), nullable = False, default = "")
    contest_id = db.Column(db.Integer, db.ForeignKey("contests.id"), nullable = False, default = "")
    students = db.relationship("Students", backref = "student", lazy = "dynamic")

    def __init__(self, name, seat_limit, room, description, contest_id):
        self.name = name
        self.seat_limit = seat_limit
        self.room = room
        self.description = description
        self.contest_id = contest_id

class Schools(db.Model):
    __tablename__ = "schools"
    id = db.Column(db.Integer, primary_key = True)
    school_name = db.Column(db.String(255), nullable = False, default = "")
    address = db.Column(db.String(255), nullable = False, default = "")
    city = db.Column(db.String(255), nullable = False, default = "") 
    zip_code = db.Column(db.String(10), nullable = False, default = "")
    school_phone = db.Column(db.String(100), nullable = False, default = "")
    username = db.Column(db.String(255), nullable = False, default = "")
    password = db.Column(db.String(255), nullable = False)
    contact_name = db.Column(db.String(255), nullable = False, default = "")
    contact_email = db.Column(db.String(255), nullable = False, default = "")
    contest_id = db.Column(db.Integer, db.ForeignKey("contests.id"), nullable = False, default = "")
    teachers = db.relationship("Teachers", backref = "teacher", lazy = "dynamic")
    students = db.relationship("Students", backref = "students", lazy = "dynamic")

    def __init__(self, school_name, address, city, zip_code, school_phone, username, password, contact_name, contact_email, contest_id):
        self.school_name = school_name
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.school_phone = school_phone
        self.username = username
        self.password = password
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contest_id = contest_id

class Teachers(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False, default = "")
    email = db.Column(db.String(255), nullable = False, default = "")
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), nullable = False, default = "")

    def __init__(self, name, email, school_id):
        self.name = name
        self.email = email
        self.school_id = school_id

class Students(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False, default = "")
    last_name = db.Column(db.String(255), nullable = False, default = "")
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), nullable = False, default = "")
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable = False, default = "")

    def __init__(self, first_name, last_name, school_id, event_id):
        self.first_name = first_name
        self.last_name = last_name
        self.school_id = school_id
        self.event_id = event_id

class Pictures(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False, default = "")
    file_name = db.Column(db.String(255), nullable = False, default = "")
    contest_id = db.Column(db.Integer, db.ForeignKey("contests.id"), nullable = False, default = "")
    ##ADD A FIELD TO STORE THE YEAR

    def __init__(self, title, file_name, contest_id):
        self.title = title
        self.file_name = file_name
        self.contest_id = contest_id

class Admins(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), nullable = False, default = "")
    password = db.Column(db.String(255), nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
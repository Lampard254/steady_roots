from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy import DateTime
from datetime import datetime

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String)
    email_subscription = db.Column(db.Boolean, default=False)
    profile = db.relationship("Profile", backref="user", uselist=False)
    experiences = db.relationship("Experience", backref="user")
    courses = db.relationship("Course", backref="user")
    memberships = db.relationship("Membership", backref="user")
    events = db.relationship("Event", backref="user")
    mentors = db.relationship("Mentor", backref="user")
    mentees = db.relationship("Mentee", backref="user")
    mailing_lists = db.relationship("Mailing_list", backref="user")
    posts = db.relationship("Post", backref="user")

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    photo_url = db.Column(db.String)
    password = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)

class Experience(db.Model):
    __tablename__ = 'experiences'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    organisation = db.Column(db.String)
    job_title = db.Column(db.String)
    description = db.Column(db.String)
    start = db.Column(DateTime, default=datetime.utcnow)
    end = db.Column(DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    level = db.Column(db.String)
    start = db.Column(DateTime, default=datetime.utcnow)
    end = db.Column(DateTime, default=datetime.utcnow)
    qualification = db.Column(db.String)

class Membership(db.Model):
    __tablename__ = 'memberships'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    amount = db.Column(db.Float)
    date_paid = db.Column(DateTime, default=datetime.utcnow)
    membership = db.Column(db.Boolean, default=False)
    expires = db.Column(DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String)
    description = db.Column(db.String)
    date = db.Column(DateTime, default=datetime.utcnow)
    image = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    approved = db.Column(db.Boolean)

class Mentor(db.Model):
    __tablename__ = 'mentors'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    description = db.Column(db.String)
    skill_id = db.Column(db.String, db.ForeignKey("skills.id"), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)

class Mentee(db.Model):
    __tablename__ = 'mentees'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    start = db.Column(DateTime, default=datetime.utcnow)
    end = db.Column(DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    mentor_id = db.Column(db.String, db.ForeignKey("mentors.id"), nullable=False)

class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    subject = db.Column(db.String)
    body = db.Column(db.Text)
    sender_email = db.Column(db.String)

class Mailing_list(db.Model):
    __tablename__ = 'mailing_list'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    email_id = db.Column(db.String, db.ForeignKey("emails.id"), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date_posted = db.Column(DateTime, default=datetime.utcnow)
    approved = db.Column(db.Boolean)
    approved_by = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String)
    mentor_id = db.Column(db.String, db.ForeignKey("mentors.id"), nullable=False)
    mentee_id = db.Column(db.String, db.ForeignKey("mentees.id"), nullable=False)

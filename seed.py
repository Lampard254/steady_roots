from app import db, app  
from models import User, Profile, Experience, Course, Membership, Event, Mentor, Mentee, Email, Mailing_list, Post, Skill
from datetime import datetime

def seed_users():
    users = [
        User(email='user1@example.com', password='password1', role='admin'),
        User(email='user2@example.com', password='password2', role='user'),
        # Add more users as needed
    ]
    with app.app_context():
        db.session.add_all(users)
        db.session.commit()
    

def seed_profiles():
    profiles = [
        Profile(first_name='John', last_name='Doe', photo_url='url1', password='password1', user_id='user1_id'),
        Profile(first_name='Jane', last_name='Smith', photo_url='url2', password='password2', user_id='user2_id'),
        # Add more profiles as needed
    ]
    with app.app_context():
        db.session.add_all(profiles)
        db.session.commit()

    
def seed_experiences():
    experiences = [
        Experience(organisation='Org1', job_title='Job1', description='Description1', start=datetime.utcnow(), end=datetime.utcnow(), user_id='user1_id'),
        Experience(organisation='Org2', job_title='Job2', description='Description2', start=datetime.utcnow(), end=datetime.utcnow(), user_id='user2_id'),
        # Add more experiences as needed
    ]
    with app.app_context():
        db.session.add_all(experiences)
        db.session.commit()
    

def seed_courses():
    courses = [
        Course(name='Course1', level='Beginner', start=datetime.utcnow(), end=datetime.utcnow(), qualification='Qualification1', user_id='user1_id'),
        Course(name='Course2', level='Intermediate', start=datetime.utcnow(), end=datetime.utcnow(), qualification='Qualification2', user_id='user2_id'),
        # Add more courses as needed
    ]
    with app.app_context():
        db.session.add_all(courses)
        db.session.commit()
    

def seed_memberships():
    memberships = [
        Membership(amount=100.0, date_paid=datetime.utcnow(), membership=True, expires=datetime.utcnow(), user_id='user1_id'),
        Membership(amount=150.0, date_paid=datetime.utcnow(), membership=False, expires=datetime.utcnow(), user_id='user2_id'),
        # Add more memberships as needed
    ]
    with app.app_context():
        db.session.add_all(memberships)
        db.session.commit()
    

def seed_events():
    events = [
        Event(name='Event1', description='Description1', date=datetime.utcnow(), image='image1', user_id='user1_id', approved=True),
        Event(name='Event2', description='Description2', date=datetime.utcnow(), image='image2', user_id='user2_id', approved=False),
        # Add more events as needed
    ]
    with app.app_context():
        db.session.add_all(events)
        db.session.commit()
    

def seed_mentors():
    mentors = [
        Mentor(description='Description1', skill_id='skill1_id', user_id='user1_id'),
        Mentor(description='Description2', skill_id='skill2_id', user_id='user2_id'),
        # Add more mentors as needed
    ]
    with app.app_context():
        db.session.add_all(mentors)
        db.session.commit()
    

def seed_mentees():
    mentees = [
        Mentee(start=datetime.utcnow(), end=datetime.utcnow(), user_id='user1_id', mentor_id='mentor1_id'),
        Mentee(start=datetime.utcnow(), end=datetime.utcnow(), user_id='user2_id', mentor_id='mentor2_id'),
        # Add more mentees as needed
    ]
    with app.app_context():
        db.session.add_all(mentees)
        db.session.commit()

    
def seed_emails():
    emails = [
        Email(subject='Subject1', body='Body1', sender_email='sender1@example.com'),
        Email(subject='Subject2', body='Body2', sender_email='sender2@example.com'),
        # Add more emails as needed
    ]
    with app.app_context():
        db.session.add_all(emails)
        db.session.commit()
    

def seed_mailing_lists():
    mailing_lists = [
        Mailing_list(email_id='email1_id', user_id='user1_id'),
        Mailing_list(email_id='email2_id', user_id='user2_id'),
        # Add more mailing lists as needed
    ]
    with app.app_context():
        db.session.add_all(mailing_lists)
        db.session.commit()
    

def seed_posts():
    posts = [
        Post(title='Title1', description='Description1', date_posted=datetime.utcnow(), approved=True, approved_by='admin', user_id='user1_id'),
        Post(title='Title2', description='Description2', date_posted=datetime.utcnow(), approved=False, approved_by=None, user_id='user2_id'),
        # Add more posts as needed
    ]
    with app.app_context():
        db.session.add_all(posts)
        db.session.commit()
    

def seed_skills():
    skills = [
        Skill(name='Skill1', mentor_id='mentor1_id', mentee_id='mentee1_id'),
        Skill(name='Skill2', mentor_id='mentor2_id', mentee_id='mentee2_id'),
        # Add more skills as needed
    ]
    with app.app_context():
        db.session.add_all(skills)
        db.session.commit()
    

def main():
    seed_users()
    seed_profiles()
    seed_experiences()
    seed_courses()
    seed_memberships()
    seed_events()
    seed_mentors()
    seed_mentees()
    seed_emails()
    seed_mailing_lists()
    seed_posts()
    seed_skills()

if __name__ == '__main__':
    main()

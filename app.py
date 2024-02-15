from models import db,User, Profile, Experience, Course, Membership, Event,MailingList, Skill, Mentor, Mentee, Post, Email
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_migrate import Migrate

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)

api = Api(app)


experience_parser = reqparse.RequestParser()
experience_parser.add_argument('organisation', type=str, required=True, help='Organisation is required')
experience_parser.add_argument('job_title', type=str, required=True, help='Job title is required')
experience_parser.add_argument('description', type=str, required=True, help='Description is required')
experience_parser.add_argument('start', type=str, required=True, help='Start date is required')
experience_parser.add_argument('end', type=str, required=True, help='End date is required')
experience_parser.add_argument('user_id', type=str, required=True, help='User ID is required')

course_parser = reqparse.RequestParser()
course_parser.add_argument('name', type=str, required=True, help='Course name is required')
course_parser.add_argument('user_id', type=str, required=True, help='User ID is required')
course_parser.add_argument('level', type=str, required=True, help='Course level is required')
course_parser.add_argument('start', type=str, required=True, help='Start date is required')
course_parser.add_argument('end', type=str, required=True, help='End date is required')
course_parser.add_argument('qualification', type=str, required=True, help='Qualification is required')

event_parser = reqparse.RequestParser()
event_parser.add_argument('name', type=str, required=True, help='Event name is required')
event_parser.add_argument('description', type=str, required=True, help='Event description is required')
event_parser.add_argument('date', type=str, required=True, help='Event date is required')
event_parser.add_argument('image', type=str, required=True, help='Event image URL is required')
event_parser.add_argument('user_id', type=str, required=True, help='User ID is required')
event_parser.add_argument('approved', type=bool, required=True, help='Event approval status is required')

class ExperienceList(Resource):
    def get(self):
        experiences = Experience.query.all()
        return [{'id': experience.experience_id, 'organisation': experience.organisation, 'job_title': experience.job_title, 'description': experience.description, 'start': experience.start, 'end': experience.end} for experience in experiences]

    def post(self):
        data = experience_parser.parse_args()
        new_experience = Experience(organisation=data['organisation'], job_title=data['job_title'], description=data['description'], start=data['start'], end=data['end'], user_id=data['user_id'])
        db.session.add(new_experience)
        db.session.commit()
        return {'message': 'Experience created successfully'}, 201

class Experience(Resource):
    def get(self, experience_id):
        experience = Experience.query.get(experience_id)
        if experience:
            return {'id': experience.experience_id, 'organisation': experience.organisation, 'job_title': experience.job_title, 'description': experience.description, 'start': experience.start, 'end': experience.end}
        else:
            return {'message': 'Experience not found'}, 404

    def patch(self, experience_id):
        data = experience_parser.parse_args()
        experience = Experience.query.get(experience_id)
        if experience:
            experience.organisation = data['organisation']
            experience.job_title = data['job_title']
            experience.description = data['description']
            experience.start = data['start']
            experience.end = data['end']
            experience.user_id = data['user_id']
            db.session.commit()
            return {'message': 'Experience updated successfully'}, 200
        else:
            return {'message': 'Experience not found'}, 404

    def delete(self, experience_id):
        experience = Experience.query.get(experience_id)
        if experience:
            db.session.delete(experience)
            db.session.commit()
            return {'message': 'Experience deleted successfully'}, 200
        else:
            return {'message': 'Experience not found'}, 404

class CourseList(Resource):
    def get(self):
        courses = Course.query.all()
        return [{'id': course.course_id, 'name': course.name, 'level': course.level, 'start': course.start, 'end': course.end, 'qualification': course.qualification} for course in courses]

    def post(self):
        data = course_parser.parse_args()
        new_course = Course(name=data['name'], user_id=data['user_id'], level=data['level'], start=data['start'], end=data['end'], qualification=data['qualification'])
        db.session.add(new_course)
        db.session.commit()
        return {'message': 'Course created successfully'}, 201

class Course(Resource):
    def get(self, course_id):
        course = Course.query.get(course_id)
        if course:
            return {'id': course.course_id, 'name': course.name, 'level': course.level, 'start': course.start, 'end': course.end, 'qualification': course.qualification}
        else:
            return {'message': 'Course not found'}, 404

    def patch(self, course_id):
        data = course_parser.parse_args()
        course = Course.query.get(course_id)
        if course:
            course.name = data['name']
            course.level = data['level']
            course.start = data['start']
            course.end = data['end']
            course.qualification = data['qualification']
            course.user_id = data['user_id']
            db.session.commit()
            return {'message': 'Course updated successfully'}, 200
        else:
            return {'message': 'Course not found'}, 404

    def delete(self, course_id):
        course = Course.query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
            return {'message': 'Course deleted successfully'}, 200
        else:
            return {'message': 'Course not found'}, 404
class EventList(Resource):
    def get(self):
        events = Event.query.all()
        return [{'id': event.event_id, 'name': event.name, 'description': event.description, 'date': event.date, 'image': event.image, 'approved': event.approved} for event in events]

    def post(self):
        data = event_parser.parse_args()
        new_event = Event(name=data['name'], description=data['description'], date=data['date'], image=data['image'], user_id=data['user_id'], approved=data['approved'])
        db.session.add(new_event)
        db.session.commit()
        return {'message': 'Event created successfully'}, 201

class Event(Resource):
    def get(self, event_id):
        event = Event.query.get(event_id)
        if event:
            return {'id': event.event_id, 'name': event.name, 'description': event.description, 'date': event.date, 'image': event.image, 'approved': event.approved}
        else:
            return {'message': 'Event not found'}, 404

    def patch(self, event_id):
        data = event_parser.parse_args()
        event = Event.query.get(event_id)
        if event:
            event.name = data['name']
            event.description = data['description']
            event.date = data['date']
            event.image = data['image']
            event.user_id = data['user_id']
            event.approved = data['approved']
            db.session.commit()
            return {'message': 'Event updated successfully'}, 200
        else:
            return {'message': 'Event not found'}, 404

    def delete(self, event_id):
        event = Event.query.get(event_id)
        if event:
            db.session.delete(event)
            db.session.commit()
            return {'message': 'Event deleted successfully'}, 200
        else:
            return {'message': 'Event not found'}, 404
        
api.add_resource(CourseList, '/courses')
api.add_resource(Course, '/courses/<string:course_id>')
api.add_resource(EventList, '/events')
api.add_resource(Event, '/events/<string:event_id>')
api.add_resource(ExperienceList, '/experiences')
api.add_resource(Experience, '/experiences/<string:experience_id>')
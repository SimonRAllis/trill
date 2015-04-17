from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://trill:@0.0.0.0:5432/trill"
db = SQLAlchemy(app)


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    managerfirstname = db.Column(db.String(80))
    managersurname = db.Column(db.String(80))

    def __init__(self, firstname, surname, email, managerfirstname, managersurname):
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.managerfirstname = managerfirstname
        self.managersurname = managersurname

    def __repr__(self):
        return '<User %r>' % self.surname


class JobTitle(db.Model):
    __tablename__ = 'job_titles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Job_Title %r>' % self.title

class TrillRoleGroup(db.Model):
    __tablename__ = 'trill_role_groups'
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(80), unique=True)
    job_title_id = db.Column(db.Integer, db.ForeignKey('job_titles.id'))

    def __init__(self, title):
        self.groupname = groupname

    def __repr__(self):
        return '<Trill_Role_Group %r>' % self.groupname

class SkillGroup(db.Model):
    __tablename__ = 'skill_groups'
    id = db.Column(db.Integer, primary_key=True)
    skillgroupname = db.Column(db.String(80), unique=True)
    trill_role_group_id = db.Column(db.Integer, db.ForeignKey('trill_role_groups.id'))

    def __init__(self, title):
        self.skillgroupname = skillgroupname

    def __repr__(self):
        return '<Skill_Group %r>' % self.skillgroupname

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    skillname = db.Column(db.String(80), unique=True)
    skill_group_id = db.Column(db.Integer, db.ForeignKey('skill_groups.id'))

    def __init__(self, title):
        self.skillname = skillname

    def __repr__(self):
        return '<Skill %r>' % self.skillname

class UserJob(db.Model):
    __tablename__ = 'user_jobs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    job_title_id = db.Column(db.Integer, db.ForeignKey('job_titles.id'))
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)

    def __init__(self, title):
        self.startdate = startdate
        self.enddate = enddate

    def __repr__(self):
        return '<User_Job %r>' % self.startdate

class UserSKill(db.Model):
    __tablename__ = 'user_skills'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
    age = db.Column(db.Date)


    def __init__(self, title):
        self.age = age

    def __repr__(self):
        return '<User_Skill %r>' % self.age



if __name__ == '__main__':
    manager.run()



'''db.drop_all()
db.create_all()
admin = User('Simon','Allis', 'simon.allis@example.com','Bev', 'Boon')
guest = User('Jim','Brown', 'jim.brown@example.com','Bev', 'Boon')

db.session.add(admin)
db.session.add(guest)
db.session.commit()



users = User.query.all()
print users

admin = User.query.filter_by(surname='Brown').first()
print admin

db.session.close() '''
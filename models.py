import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'blood_donation_system')
# database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
database_path='postgres://atyqejusvixadd:9aeeb8c28abcc0c4f5be39e6f93fea50f3e962f44b73ecfa6450260acb63289e@ec2-54-85-13-135.compute-1.amazonaws.com:5432/dclm7h9kc6hijf'
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all()


'''
Donor
'''
class Donor(db.Model):  

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  address = Column(String)
  phone = Column(String)
  email = Column (String)
  blood_type = Column (String)
  
  donation = db.relationship( 'Donation', backref=db.backref('donor', cascade='all, delete'))


  def __init__(self, name, age, gender, address, phone, email, blood_type):
    self.name = name
    self.age = age
    self.gender = gender
    self.address = address
    self.phone = phone
    self.email = email
    self.blood_type = blood_type

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name' : self.name,
      'age' :self.age,
      'gender' : self.gender,
      'address' : self.address,
      'phone' : self.phone, 
      'email' : self.email,
      'blood_type' :self.blood_type
    }


'''
Donation
'''
class Donation(db.Model):  

  id = Column(Integer, primary_key=True)
  blood_type = db.Column(db.String)
  time=db.Column(db.DateTime())
  donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'))
  donationCenter_id= db.Column(db.Integer, db.ForeignKey('donation_center.id'))


  def __init__(self, donor_id, blood_type, time, donationCenter_id):
    self.donor_id = donor_id
    self.blood_type = blood_type
    self.time = time
    self.donationCenter_id = donationCenter_id

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'donor_id': self.donor_id,
      'blood_type': self.blood_type,
      'donationCenter_id': self.donationCenter_id,
      'time': self.time
    }


'''
Donation Center
'''
class DonationCenter(db.Model):  

  id = Column(Integer, primary_key=True)
  name = db.Column(db.String)
  address = db.Column(db.String)

  donations = db.relationship( 'Donation', backref=db.backref('donation_center', cascade='all, delete'))
  appointments = db.relationship( 'Appointment', backref=db.backref('donation_center', cascade='all, delete'))

  def __init__(self, name, address):
    self.name=name,
    self.address = address

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name' : self.name,
      'address': self.address
    }




'''
Appointment
'''
class Appointment(db.Model):  

  id = Column(Integer, primary_key=True)
  donations_center = db.Column(db.Integer, db.ForeignKey('donation_center.id'))
  time=db.Column(db.DateTime())
  donors_limit = db.Column(db.Integer)
  availibility = db.Column(db.Boolean, default=True)


  def __init__(self,donations_center, time,donors_limit, availibility):
    self.donations_center = donations_center
    self.time=time
    self.donors_limit=donors_limit
    self.availibility=availibility


  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'donations_center': self.donations_center,
      'time': self.time
    }


class AppointmentsDonors(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'))
  appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'))
  donor = db.relationship( Donor, backref=db.backref('appointments_donors', cascade='all, delete'))
  appointment = db.relationship( Appointment, backref=db.backref('appointments_donors', cascade='all, delete'))
  
  def __init__(self,donor_id,appointment_id):
    self.donor_id = donor_id
    self.appointment_id=appointment_id

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def format(self):
    return {
      'id': self.id,
      'appointment_id': self.appointment_id,
      'donor_id': self.donor_id
    }
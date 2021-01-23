import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import *
from auth import *


RESULTS_PER_PAGE = 10


# https://dev-16nawflo.us.auth0.com/authorize?audience=blood_donation&response_type=token&client_id=gMdV5Kv5iDUPf9JTuG9oqrFfRwYVAFfr&redirect_uri=http://localhost:5000
# AUTH0_DOMAIN="dev-16nawflo.us.auth0.com"
# AUTH0_CLIENT_ID="gMdV5Kv5iDUPf9JTuG9oqrFfRwYVAFfr"
# AUTH0_JWT_API_AUDIENCE="blood_donation"

def paginate_results(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RESULTS_PER_PAGE
    end = start + RESULTS_PER_PAGE

    results = [result.format() for result in selection]
    current_results = results[start:end]
    return current_results

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  db = setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type, Authorization')
      response.headers.add(
          'Access-Control-Allow-Methods',
          'GET, POST, PATCH, DELETE, OPTIONS')
      return response

  @app.route('/donors')
  @requires_auth('get:donors')
  def retrive_donors(auth):
      donors = Donor.query.all()
      if donors is None or len(donors) == 0:
          abort(404)
      selection = Donor.query.order_by(Donor.id).all()
      current_donors= paginate_results(request, selection)
      return jsonify({
          'success': True,
          'donors': current_donors,
          'donors_count': len(Donor.query.all())
      })

  @app.route('/donations')
  def retrive_donations():
      donations = Donation.query.all()
      print(donations)
      if donations is None or len(donations) == 0:
          abort(404)
      length = len(donations)
      selection = Donation.query.order_by(Donation.id).all()
      current_donations= paginate_results(request, selection)
      return jsonify({
          'success': True,
          'current_donations': current_donations,
          'current_donations_count': len(Donation.query.all())
      })


  @app.route('/donation_centers')
  def retrive_donation_centers():
      donation_centers = DonationCenter.query.all()
      if donation_centers is None or len(donation_centers) == 0:
          abort(404)
      length = len(donation_centers)
      selection = DonationCenter.query.order_by(DonationCenter.id).all()
      current_donation_centers= paginate_results(request, selection)
      return jsonify({
          'success': True,
          'current_donation_centers': current_donation_centers,
          'current_donation_centers_count': len(DonationCenter.query.all())
      })

  @app.route('/appointments')
  @requires_auth('get:appointments')
  def retrive_appointments(auth):
      appointments = Appointment.query.all()
      if appointments is None or len(appointments) == 0:
          abort(404)
      length = len(appointments)
      selection = Appointment.query.order_by(Appointment.id).all()
      current_appointments= paginate_results(request, selection)
      return jsonify({
          'success': True,
          'current_donation_centers': current_appointments,
          'current_donation_centers_count': len(Appointment.query.all())
      })

  @app.route('/appointments_donors')
  @requires_auth('get:appointments_donors')
  def retrive_appointments_donors(auth):
      appointments_donors = AppointmentsDonors.query.all()
      if appointments_donors is None or len(appointments_donors) == 0:
          abort(404)
      length = len(appointments_donors)
      selection = AppointmentsDonors.query.order_by(AppointmentsDonors.id).all()
      current_appointments_donors= paginate_results(request, selection)
      return jsonify({
          'success': True,
          'current_appointments_donors': current_appointments_donors,
          'current_appointments_donors_count': len(Appointment.query.all())
      })

  @app.route('/DonationCenter', methods=['POST'])
  @requires_auth('create:DonationCenter')
  def create_donation_center(auth):
      body = request.get_json()
      new_name= body.get('name', None)
      new_address = body.get('address', None)
      try:
          if new_name and new_address:
              donation_center = DonationCenter(
                  name=new_name,
                  address=new_address)
              donation_center.insert()

              selection = DonationCenter.query.order_by(DonationCenter.id).all()
              current_centers = paginate_results(request, selection)

              return jsonify({
                  'success': True,
                  'created': donation_center.id,
                  'donation_centers': current_centers,
                  'donation_centers_count': len(DonationCenter.query.all())
              })
          else:
              abort(404)
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)



  
  @app.route('/Appointment', methods=['POST'])
  @requires_auth('create:Appointment')
  def create_appointment(auth):
      body = request.get_json()
      new_donations_center= body.get('donations_center', None)
      new_time = body.get('time', None)
      new_donors_limit = body.get('donors_limit', None)
      new_availibility= body.get('availibility', None)
      try:
          if new_donations_center and new_time and new_donors_limit:
              appointment = Appointment(
                  donations_center=new_donations_center,
                  time=new_time,
                  donors_limit=new_donors_limit,
                  availibility=new_availibility)
              print(appointment)
              appointment.insert()

              selection = Appointment.query.order_by(Appointment.id).all()
              current_appointments = paginate_results(request, selection)

              return jsonify({
                  'success': True,
                  'created': appointment.id,
                  'appointments': current_appointments,
                  'appointments_count': len(Appointment.query.all())
              })
          else:
              abort(404)
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)

  
  
  @app.route('/Donor', methods=['POST'])
  @requires_auth('create:Donor')
  def create_donor(auth):
      body = request.get_json()
      new_name= body.get('name', None)
      new_age = body.get('age', None)
      new_gender = body.get('gender', None)
      new_address = body.get('address', None)
      new_phone= body.get('phone', None)
      new_email= body.get('email',None)
      new_blood_type= body.get('blood_type', None)
      try:
          if new_name and new_age and new_gender and new_phone and new_email and new_blood_type:
              donor = Donor(
                  name=new_name,
                  age=new_age,
                  gender=new_gender,
                  address = new_address,
                  phone=new_phone,
                  email=new_email,
                  blood_type=new_blood_type)
              donor.insert()

              selection = Donor.query.order_by(Donor.id).all()
              current_donors= paginate_results(request, selection)

              return jsonify({
                  'success': True,
                  'created': donor.id,
                  'donors': current_donors,
                  'donors_count': len(Donor.query.all())
              })
          else:
              abort(404)
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)



  @app.route('/Donation', methods=['POST'])
  @requires_auth('create:Donation')
  def create_donation(auth):
      body = request.get_json()
      new_donationCenter_id= body.get('donationCenter_id', None)
      new_donor_id=body.get('donor_id', None)
      new_blood_type= body.get('blood_type', None)
      new_time = body.get('time', None)
      try:
          if new_donationCenter_id and new_donor_id and new_blood_type and new_time:
              donation = Donation(
                  donationCenter_id=new_donationCenter_id,
                  donor_id=new_donor_id,
                  blood_type=new_blood_type,
                  time=new_time)
              donation.insert()

              selection = Donation.query.order_by(Donation.id).all()
              current_donations = paginate_results(request, selection)

              return jsonify({
                  'success': True,
                  'created': donation.id,
                  'donations': current_donations,
                  'donations_count': len(Donation.query.all())
              })
          else:
              abort(400)
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)



  @app.route('/AppointmentsDonors', methods=['POST'])
  @requires_auth('create:AppointmentsDonors')
  def create_AppointmentsDonors(auth):
      body = request.get_json()
      new_donor_id=body.get('donor_id', None)
      new_appointment_id = body.get('appointment_id', None)
      try:
          if new_donor_id and new_appointment_id:
              appointmentDonor = AppointmentsDonors(
                  appointment_id=new_appointment_id,
                  donor_id=new_donor_id
                  )
              appointmentDonor.insert()

              selection = AppointmentsDonors.query.order_by(AppointmentsDonors.id).all()
              current_appointmentsDonors = paginate_results  (request, selection)

              return jsonify({
                  'success': True,
                  'created': appointmentDonor.id,
                  'appointmentsDonors': current_appointmentsDonors,
                  'appointmentsDonors_count': len(AppointmentsDonors.query.all())
              })
          else:
              abort(404)
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)


  @app.route('/donors/<int:donor_id>', methods=['DELETE'])
  @requires_auth('delete:donors')
  def delete_donor(auth,donor_id):
      try:
          donor = Donor.query.filter(
              Donor.id == donor_id).one_or_none()
          if donor is None:
              abort(404)
          donor.delete()
          selection = Donor.query.order_by(Donor.id).all()
          current_donors = paginate_results(request, selection)
          return jsonify({
              'success': True,
              'deleted': donor_id,
              'donors': current_donors,
              'total_donors': len(Donor.query.all())
          })
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)

  @app.route('/donors/<int:donor_id>', methods=['PATCH'])
  @requires_auth('update:donor')
  def update_donor(auth,donor_id):
      body = request.get_json()
      donor = Donor.query.filter(
              Donor.id == donor_id).one_or_none()
      try:
          print("I am here")
          donor.name= body.get('name', donor.name)
          donor.age = body.get('age', donor.age)
          donor.gender = body.get('gender', donor.age)
          donor.phone= body.get('phone', donor.phone)
          donor.email= body.get('email', donor.email)
          donor.blood_type= body.get('blood_type', donor.blood_type)
          donor.update()
          return jsonify({
                  'success': True,
                  'created': donor.id,
                  'donors_count': len(Donor.query.all())
              })
      except Exception as error:
          print("\nerror => {}\n".format(error))
          abort(422)

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422



  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"
      }), 400

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404


  @app.errorhandler(AuthError)
  def authentification_failed(error):
      return jsonify({
          "success": False,
          "error": AuthError,
          "message": "authentification fails"
                      }), AuthError
  return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)





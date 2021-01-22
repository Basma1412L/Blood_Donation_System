import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import *


DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_TEST_NAME = os.getenv('DB_NAME', 'blood_system_test')
database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_TEST_NAME)
Token_manager="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkkzbktsM2lST0FNM21odjhjSm9hQiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xNm5hd2Zsby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYTBiMDg3ZmM5MTQwMDY5OWE5YWI0IiwiYXVkIjoiYmxvb2RfZG9uYXRpb24iLCJpYXQiOjE2MTEyOTc4NzMsImV4cCI6MTYxMTMwNTA3MywiYXpwIjoiZ01kVjVLdjVpRFVQZjlKVHVHOW9xckZmUndZVkFGZnIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpBcHBvaW50bWVudCIsImNyZWF0ZTpBcHBvaW50bWVudHNEb25vcnMiLCJjcmVhdGU6RG9uYXRpb24iLCJjcmVhdGU6RG9uYXRpb25DZW50ZXIiLCJjcmVhdGU6RG9ub3IiLCJkZWxldGU6ZG9ub3JzIiwiZ2V0OmFwcG9pbnRtZW50cyIsImdldDphcHBvaW50bWVudHNfZG9ub3JzIiwiZ2V0OmRvbmF0aW9ucyIsImdldDpkb25vcnMiLCJ1cGRhdGU6ZG9ub3IiXX0.Dip_kPW_nbfxI23Soh_Qhq6wSL3A1RqP2_bpDzbWvvDp5pGdche_dRzeh9b4E6tPv0Mp5FJYOoNnVvtLvLmVXmZ_-rcMl-40SMVAPU5S65yYehgNVaXzozGnIC_vwSB7jXpY4JvmaPQD9boA3EebQYJGf_kWAK9o_9IESjb16wahPKqFYuQddBVFUg0c8E_KLfZOwzO6FAIuO6VSshnqwYZzXqB4FLeKThP9_uQA0nSafNX0JhlksqnbH6mCY5pf9DkKVr1EwTJIaqaRnWsIHscvtz8BDO33YutYMLFeWlLaXtcSHe02APxLA-NKrQOKm1G5eWvd5m5YqtcEJ4_cZw"
Token_donor="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkkzbktsM2lST0FNM21odjhjSm9hQiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xNm5hd2Zsby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwOTIwZDM1MTg1M2IwMDZhMDA5N2Y0IiwiYXVkIjoiYmxvb2RfZG9uYXRpb24iLCJpYXQiOjE2MTEzMDA4ODksImV4cCI6MTYxMTMwODA4OSwiYXpwIjoiZ01kVjVLdjVpRFVQZjlKVHVHOW9xckZmUndZVkFGZnIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpEb25hdGlvbiIsImNyZWF0ZTpEb25vciIsImdldDphcHBvaW50bWVudHMiLCJnZXQ6YXBwb2ludG1lbnRzX2Rvbm9ycyJdfQ.rO9P4HSnG1zHM5e7p-gz3kDhaTNcHUPnGIKc0b6TdQSnKGFEQwMtbEzmaaqmDGYe2g3K-nbUar7zUA9uaa5obpC6Vv0sniTTOQaB3gPA_rQoaQmXGNnGu9h3FA-sjqjG5L1p8H7JojWhNqVX2PWLtF_CDC1Abhilh8HhaVsSBtWcAMERCOfukDyrWQkO54A62QN-Hdsi21cRjiW2T-VECMWfcbKXfwisJ3FTtfS_ti4KsIUXPJ60dhfzUPKIfycho6DNeDMtfCoHO8WtK16_ScA4T11wkJ7EMBstA3DD1Y_LwkyD1J4OUSkkkGEZ8eM5vnZ1YQbnsskwYOoHd8cDKg"
headers = {    'Content-Type': 'application/json',
'Authorization': 'Bearer '+ Token_manager
            }
headers_donor= {  'Content-Type': 'application/json',
'Authorization': 'Bearer '+ Token_donor
                }
class BloodSystemTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path=database_path
        setup_db(self.app, self.database_path)
        self.headers=headers
        self.headers_donor=headers_donor

        self.new_donor = {
        "name" : "Radi",
        "age" : 25,
        "gender" : "Male",
        "address" : "290 Bath Road",
        "phone" : "3433336460",
        "email" : "radi@gmail.com",
        "blood_type" : "A+" }

        self.updated_donor = {
        "id" : 33,
        "name" : "Radi",
        "age" : 25,
        "gender" : "Male",
        "address" : "290 Bath Road",
        "phone" : "3433336460",
        "email" : "Rabab@gmail.com",
        "blood_type" : "A+" }

        self.new_donation_center = {
        "name" : "Downtown Donation Center",
        "address" : "159 King Road" }

        self.new_donation =     {
        "blood_type" :"A+",
        "time" : "2021-01-01 10:05:03",
         "donor_id": 35,
         "donationCenter_id" : 1
    }

        self.new_appontment = {
        "donations_center" : 1,
        "time" : "2021-01-01 10:05:03",
        "donors_limit" : 5,
        "availibility" : True }

        self.new_appointmentsDonors ={
            "donor_id" : 31,
            "appointment_id" : 2  }

        # binds the app to the current context
        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
        #     # create all tables
        #     self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass



    def test_retrive_donors(self):
        res = self.client().get('/donors',headers=self.headers)
        print(res)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donors'])

    

    def fail_test_retrive_donors(self):
        res = self.client().get('/donors/8',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)



    def test_retrive_donations(self):
        res = self.client().get('/donations',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_donations'])
  
    
    def fail_test_retrive_donors(self):
        res = self.client().get('/donations/7',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    
    def test_retrive_appointments_donors(self):
        res = self.client().get('/appointments_donors',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_appointments_donors'])
  
    
    def fail_test_retrive_appointments_donors(self):
        res = self.client().get('/appointments_donors/7',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_success_create_donation_center(self):
        res = self.client().post('/DonationCenter', json=self.new_donation_center,headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donation_centers'])
        self.assertTrue(data['donation_centers_count'])

    def test_fail_create_donation_center(self):
        res = self.client().post('/questions/45', json=self.new_donation_center,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_appointment(self):
        res = self.client().post('/Appointment', json=self.new_appontment,headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['appointments'])
        self.assertTrue(data['appointments_count'])

    def test_fail_create_appointment(self):
        res = self.client().post('/Appointment/45', json=self.new_appontment,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_success_create_donor(self):
        res = self.client().post('/Donor', json=self.new_donor,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donors'])
        self.assertTrue(data['donors_count'])

    def test_fail_create_donor(self):
        res = self.client().post('/Donor/45', json=self.new_donor,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_success_create_donation(self):
        res = self.client().post('/Donation', json=self.new_donation,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_create_donation(self):
        res = self.client().post('/Donation/7', json=self.new_donation,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_AppointmentsDonors(self):
        res = self.client().post('/AppointmentsDonors', json=self.new_appointmentsDonors,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['appointmentsDonors'])
        self.assertTrue(data['appointmentsDonors_count'])

    def test_fail_create_AppointmentsDonors(self):
        res = self.client().post('/AppointmentsDonors/7', json=self.new_appointmentsDonors,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_success_delete_donor(self):
        res = self.client().delete('/donors/36',headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 36).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_donors'])
        self.assertEqual(donor, None)

    def test_fail_delete_donor(self):
        res = self.client().delete('/donors/5000',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


    def test_success_update_donor(self):
        res = self.client().patch('/donors/35',json=self.updated_donor,headers=self.headers)
        print(res)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_update_donor(self):
        res = self.client().patch('/donors/5000',json=self.updated_donor,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)




    def test_success_delete_donor_manager(self):
        res = self.client().delete('/donors/33',headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 33).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(donor, None)

    def test_fail_delete_donor_authentication(self):
        res = self.client().delete('/donors/5000',headers=self.headers_donor)
        self.assertEqual(401, res.status_code)





# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
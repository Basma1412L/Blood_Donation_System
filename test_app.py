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
Token_manager = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkkzbktsM2lST0FNM21odjhjSm9hQiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xNm5hd2Zsby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwOGIwMTI0NDFmZDYwMDcwODFhOGFmIiwiYXVkIjoiYmxvb2RfZG9uYXRpb24iLCJpYXQiOjE2MTE0NDgxOTIsImV4cCI6MTYxMTQ1NTM5MiwiYXpwIjoiZ01kVjVLdjVpRFVQZjlKVHVHOW9xckZmUndZVkFGZnIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpBcHBvaW50bWVudCIsImNyZWF0ZTpBcHBvaW50bWVudHNEb25vcnMiLCJjcmVhdGU6RG9uYXRpb24iLCJjcmVhdGU6RG9uYXRpb25DZW50ZXIiLCJjcmVhdGU6RG9ub3IiLCJkZWxldGU6ZG9ub3JzIiwiZ2V0OmFwcG9pbnRtZW50cyIsImdldDphcHBvaW50bWVudHNfZG9ub3JzIiwiZ2V0OmRvbmF0aW9ucyIsImdldDpkb25vcnMiLCJ1cGRhdGU6ZG9ub3IiXX0.NNKVw9X_5aDXHj50rC_5H5s194tYRdR9lmG1R4xCfRwleKleBjZZE2pKrPkrEZwpf8NxJtEwCvGTqJbc_avek_iyYYRO0j6K2y4pJfIq_a-7GaFPyhxAfckDccHC084A8WirpEVKj2P9NHHgfW3mI4UxXfozjMT69Zbq0DtRhpVyLfomAkieoCTRwsVRFp57ZDR-B1QU-nErQeIucElBRcrMVRNAIwlS9iLb1ucRECIBfwJN4wPCb4RdLGoOPQzlSZJnFnJKRQv-eobAgtksavVemIbva1Xsn75V1DqBnTy_97IR7GXon7NLaLvizhJe1hWk8w8otYtOXIss13CS2Q"
Token_donor = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkkzbktsM2lST0FNM21odjhjSm9hQiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xNm5hd2Zsby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYTBiMjQ3ZmM5MTQwMDY5OWE5YWJiIiwiYXVkIjoiYmxvb2RfZG9uYXRpb24iLCJpYXQiOjE2MTE0NDg0MjcsImV4cCI6MTYxMTQ1NTYyNywiYXpwIjoiZ01kVjVLdjVpRFVQZjlKVHVHOW9xckZmUndZVkFGZnIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpEb25hdGlvbiIsImNyZWF0ZTpEb25vciIsImdldDphcHBvaW50bWVudHMiLCJnZXQ6YXBwb2ludG1lbnRzX2Rvbm9ycyJdfQ.T1hBE_LY825D3GQV1ZDSScr8VI4y2e2Xt-X9SIg-YIamF0aUlhdnM9nsiW2nTwRRFve0VhRD0EDStn-sm6rBNfMqVZW0W-992EF5jCpMyvw8JJASULtoYdOVKiBbIGuvyFHApBUi-OLoRTspSv8eUYfV1MDdQupJ4MhdQakbabtDwuM04vhS7u0TLm_20RyaIZmHANV52H86P6IEVOPt00CSF3JFsZJp8nf3aUKJLowKETLrqK7ZFI-OYUno_uTFQYoTeaYTax2Uww_rh84smXfjZawzNdQiaJp0Y1jD47fTECp6gYdchIDC0pvy-8SI0P_3ypiy58NnuDFL0Pp-qg"
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + Token_manager
           }
headers_donor = {'Content-Type': 'application/json',
                 'Authorization': 'Bearer ' + Token_donor
                 }


class BloodSystemTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        self.headers = headers
        self.headers_donor = headers_donor

        self.new_donor = {
            "name": "Radi",
            "age": 25,
            "gender": "Male",
            "address": "290 Bath Road",
            "phone": "3433336460",
            "email": "radi@gmail.com",
            "blood_type": "A+"}

        self.updated_donor = {
            "id": 33,
            "name": "Radi",
            "age": 25,
            "gender": "Male",
            "address": "290 Bath Road",
            "phone": "3433336460",
            "email": "Rabab@gmail.com",
            "blood_type": "A+"}

        self.new_donation_center = {
            "name": "Downtown Donation Center",
            "address": "159 King Road"}

        self.new_donation = {
            "blood_type": "A+",
            "time": "2021-01-01 10:05:03",
            "donor_id": 35,
            "donationCenter_id": 1
        }

        self.new_appontment = {
            "donations_center": 1,
            "time": "2021-01-01 10:05:03",
            "donors_limit": 5,
            "availibility": True}

        self.new_appointmentsDonors = {
            "donor_id": 31,
            "appointment_id": 2}

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
        res = self.client().get('/donors', headers=self.headers)
        print(res)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donors'])

    def fail_test_retrive_donors(self):
        res = self.client().get('/donors/8', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_retrive_donations(self):
        res = self.client().get('/donations', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_donations'])

    def fail_test_retrive_donors(self):
        res = self.client().get('/donations/7', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_retrive_appointments_donors(self):
        res = self.client().get('/appointments_donors', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_appointments_donors'])

    def fail_test_retrive_appointments_donors(self):
        res = self.client().get('/appointments_donors/7', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_donation_center(self):
        res = self.client().post(
            '/DonationCenter',
            json=self.new_donation_center,
            headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donation_centers'])
        self.assertTrue(data['donation_centers_count'])

    def test_fail_create_donation_center(self):
        res = self.client().post(
            '/questions/45',
            json=self.new_donation_center,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_appointment(self):
        res = self.client().post(
            '/Appointment',
            json=self.new_appontment,
            headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['appointments'])
        self.assertTrue(data['appointments_count'])

    def test_fail_create_appointment(self):
        res = self.client().post(
            '/Appointment/45',
            json=self.new_appontment,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_donor(self):
        res = self.client().post('/Donor', json=self.new_donor, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donors'])
        self.assertTrue(data['donors_count'])

    def test_fail_create_donor(self):
        res = self.client().post('/Donor/45', json=self.new_donor, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_donation(self):
        res = self.client().post(
            '/Donation',
            json=self.new_donation,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_create_donation(self):
        res = self.client().post(
            '/Donation/7',
            json=self.new_donation,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_create_AppointmentsDonors(self):
        res = self.client().post(
            '/AppointmentsDonors',
            json=self.new_appointmentsDonors,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['appointmentsDonors'])
        self.assertTrue(data['appointmentsDonors_count'])

    def test_fail_create_AppointmentsDonors(self):
        res = self.client().post(
            '/AppointmentsDonors/7',
            json=self.new_appointmentsDonors,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_success_delete_donor(self):
        res = self.client().delete('/donors/36', headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 36).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_donors'])
        self.assertEqual(donor, None)

    def test_fail_delete_donor(self):
        res = self.client().delete('/donors/5000', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_success_update_donor(self):
        res = self.client().patch(
            '/donors/35',
            json=self.updated_donor,
            headers=self.headers)
        print(res)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_update_donor(self):
        res = self.client().patch(
            '/donors/5000',
            json=self.updated_donor,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_success_delete_donor_manager(self):
        res = self.client().delete('/donors/33', headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 33).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(donor, None)

    def test_fail_delete_donor_authentication(self):
        res = self.client().delete('/donors/5000', headers=self.headers_donor)
        self.assertEqual(401, res.status_code)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

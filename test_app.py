import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category


class BloodSystemTestCase(unittest.TestCase):
    DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
    DB_USER = os.getenv('DB_USER', '')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_TEST_NAME = os.getenv('DB_NAME', 'blood_system_test')
    database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_TEST_NAME)
    Token_manager=""
    Token_donor=""
    headers = { "Authorization: "Basic" ' + "Token_manager"
                }
    headers_donor= { "Authorization: "Basic" ' + "Token_donor"
                }


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, self.database_path)
        self.headers=headers
        self.headers_donor=headers_donor

        self.new_question = {
            'question': 'What is the sign of 2020?',
            'answer': 'Covid19',
            'category': 1,
            'difficulty': 1
        }

        self.quiz = {
            'quiz_category': {'type': 'Science', 'id': '1'},
            'previous_questions': [
                'What is the disease of 2020?',
                'What is the loss of 2020?']}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass



    def test_retrive_donors(self):
        res = self.client().get('/donors',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donors'])
        self.assertTrue(data['total_donors'])

    

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
        self.assertTrue(data['total_donations'])
        self.assertTrue(data['total_donations'])
  
    
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
        self.assertTrue(data['appointments_donors'])
        self.assertTrue(data['total_appointments_donors'])
  
    
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
        res = self.client().post('/Appointment/45', json=self.new_donor,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_success_create_donation(self):
        res = self.client().post('/Donation', json=self.new_donation,headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['donations'])
        self.assertTrue(data['donations_count'])

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
        res = self.client().delete('/donors/1',headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 20).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 20)
        self.assertTrue(data['total_donors'])
        self.assertEqual(donor, None)

    def test_fail_delete_donor(self):
        res = self.client().delete('/donors/5000',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    def test_success_update_donor(self):
        res = self.client().delete('/donors/1',headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['donors_count'])

    def test_fail_update_donor(self):
        res = self.client().delete('/donors/5000',headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')




    def test_success_delete_donor_manager(self):
        res = self.client().delete('/donors/1',headers=self.headers)
        data = json.loads(res.data)
        donor = Donor.query.filter(Donor.id == 20).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 20)
        self.assertTrue(data['total_donors'])
        self.assertEqual(donor, None)

    def test_fail_delete_donor_authentication(self):
        res = self.client().delete('/donors/5000',headers=self.headers_donor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
Motivation:
The goal of this project is to ease the process of blood donation for both the donors and the donation centers. Where the donors can easily find the locations of the blood donation centers and know the available appointments in each center. And the managers can access the donations and the blood_types that are donated to know what shortage do they have and what types do they need more.

Overview:
This application is the backend of a blood donation system. The application allows donor to locatios of the donation centers that they can donate in and allow the managers to add appointments and add the donations to the system.

Roles:
There are two main roles:
1 - Manager: Person who can:
  "create:Appointment",
    "create:AppointmentsDonors",
    "create:Donation",
    "create:DonationCenter",
    "create:Donor",
    "delete:donors",
    "get:appointments",
    "get:appointments_donors",
    "get:donations",
    "get:donors",
    "update:donor"

2 - Donor: Person who can:
    "create:Donation",
    "create:Donor",
    "get:appointments",
    "get:appointments_donors"


  To run the project:

  1- clone the project from the git repo 

  2- use an enviroment and activate it (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

  3- Install all the requirements using:  pip install -r requirements.txt

  4- set env variables: set FLASK_APP=app.py && set FLASK_ENV=development

  5- create a database called blood_system_test for testing the database
  enter random data for the sake of testing using psql
  i.e: 
   insert into donor (name, age, gender, address, phone , email, blood_type) values ('Alia', 20, 'Female', '290 Bath Road', '3433336460', 'alia@gmail.com', 'A+');
 insert into donor (name, age, gender, address, phone , email, blood_type) values ('Ali', 20, 'Male', '290 Bath Road', '3433336460', 'ali@gmail.com', 'A+');
 insert into donation_center (name, address) values ('Downttown2 center', 'downtown');
 insert into donation_center (name, address) values ('Downttown1 center', 'downtown');
 insert into donation (blood_type, time, donor_id, "donationCenter_id") values ('A+', '2021-01-01 11:05:03', 1,1);
  insert into donation (blood_type, time, donor_id, "donationCenter_id") values ('A+', '2021-01-01 11:05:03', 1,1);
  insert into appointment (donations_center ,time, donors_limit, availibility) values (1, '2021-01-01 11:05:03', 5,true);
   insert into appointment (donations_center ,time, donors_limit, availibility) values (2, '2021-01-01 11:05:03', 5,true);
    insert into appointments_donors (donor_id ,appointment_id ) values (1,1);
 insert into appointments_donors (donor_id ,appointment_id ) values (2,2);

6- check the ids in created database and make sure that the ids in the APIs exist; don't try to use non existant ids because they won't work 

7- python test.py to run the test module

8- to check the project locally before using heroku uncomment this line in the models.py module # database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME) and use the local database in the same way as we did in the testing

9- comment the line again and check heroku 

10- and never forget: flask run or python app.py to run the module 

### Endpoint Library

Get (('/donors'))
Returns a list of all available donors
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/donors 
Sample response output:
{
  "donors" = [
    {
        "name" : "Ramy",
        "age" : 25,
        "gender" : "Male",
        "address" : "290 Bath Road",
        "phone" : "3433336460",
        "email" : "ramy@gmail.com",
        "blood_type" : "A+"
    },
    {
        "name" : "Hady",
        "age" : 25,
        "gender" : "Male",
        "address" : "290 Bath Road",
        "phone" : "3433336460",
        "email" : "hady@gmail.com",
        "blood_type" : "B+"
    }, 
    {
        "name" : "Mona",
        "age" : 25,
        "gender" : "FeMale",
        "address" : "290 Bath Road",
        "phone" : "3433336460",
        "email" : "mona@gmail.com",
        "blood_type" : "O-"
    }
]
}

Get (('/donations'))
Returns a list of all available donations
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/donations 
Sample response output:
{
  "donations" = [
    {
        "blood_type" :"A+",
        "time" : "2021-01-01 10:05:03",
         "donor_id" :  1
         "donationCenter_id" : 1
    }, 
    {
        "blood_type" :"B+",
        "time" : "2021-01-01 11:05:03",
         "donor_id" :  2
         "donationCenter_id" : 2
    },
    {
        "blood_type" :"O-",
        "time" : "2021-01-01 10:05:03",
         "donor_id" :  3
         "donationCenter_id" : 3
    }
]
}



Get (('/donation_centers'))
Returns a list of all available donation centers 
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/donation_centers 
Sample response output:
{
  "donation_centers" = [
    {
        "name" : "Downtown Donation Center",
        "address" : "159 King Road"
    },
    {
        "name" : "King Donation Center",
        "address" : "172 Palace Road"
    },
    {
        "name" : "ETL Donation Center",
        "address" : "23 Ring Road"
    }
]
}


Get (('/appointments'))
Returns a list of all available appointments 
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/appointments 
Sample response output:
{
  "appointments" = [
    {
        "donations_center" : 1,
        "time" : "2021-01-01 10:05:03",
        "donors_limit" : 5,
        "availibility" : True
    },
    {
        "donations_center" : 2,
        "time" : "2021-01-01 10:05:03",
        "donors_limit" : 3,
        "availibility" : True
    },
    {
        "donations_center" : 3,
        "time" : "2021-01-01 09:05:03",
        "donors_limit" : 1,
        "availibility" : False
    }
]
}


et (('/appointments_donors'))
Returns a list of all available appointments_donors  
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/appointments 
Sample output:
{
  "appointmentsDonors" = [
    {
        "donor_id" : 1,
        "appointment_id" : 2 
    }, 
        {
        "donor_id" : 2,
        "appointment_id" : 2 
    },    {
        "donor_id" : 3,
        "appointment_id" : 3 
    }
]
}


POST '/DonationCenter'
Create a new donation center and Returns a list of all Donation Centers , along with new center posted, a success value, and total number of donation centers.
Sample curl: 
curl http://localhost:5000/DonationCenter -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{
        "name" : "Downtown Donation Center",
        "address" : "159 King Road"
    }'



POST '/Appointment'
Create a new appointment and Returns a list of all  appointments , along with new appointment posted, a success value, and total number of appointments.
Sample curl: 
curl http://localhost:5000/Appointment -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '    {
        "donations_center" : 2,
        "time" : "2021-01-01 10:05:03",
        "donors_limit" : 3,
        "availibility" : True
    }'



POST '/Donor'
Create a new appointment and Returns a list of all  donors , along with new donor posted, a success value, and total number of donors.
Sample curl: 
curl http://localhost:5000/Donor -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d ' {
        "name" : "Mona",
        "age" : 25,
        "gender" : "FeMale",
        "address" : "290 Bath Road",
        "phone" : "3433336460",
        "email" : "mona@gmail.com",
        "blood_type" : "O-"
    }'




POST '/Donation'
Create a new donation and Returns a list of all  donations , along with new donation posted, a success value, and total number of donations.
Sample curl: 
curl http://localhost:5000/Donation -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '     {
        "blood_type" :"A+",
        "time" : "2021-01-01 10:05:03",
         "donor_id" :  1
         "donationCenter_id" : 1
    }'


POST '/AppointmentsDonors'
Create a new appointmetsfordonor and Returns a list of all  AppointmentsDonors , along with new AppointmentsDonors posted, a success value, and total number of AppointmentsDonors.
Sample curl: 
curl http://localhost:5000/AppointmentsDonors -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{
        "donor_id" : 1,
        "appointment_id" : 2 
    }'


DELETE '/donors/<int:donor_id>'
delete a  donor with the sent id  and Returns  the id of the deleted donor, a list of all  donors without the deleted donor , a success value, and total number of donors.
Sample curl: 
curl http://localhost:5000//donors/1 -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d


PATCH '/donors/<int:donor_id>'
update a  donor with the sent id  and Returns  the id of the updated donor, a list of all  donors with the updated donor , a success value, and total number of donors.
Sample curl: 
curl http://localhost:5000//donors/1 -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{ "blood_type" : "O-"
    }'


Heroku URL:
https://blood0donations.herokuapp.com/



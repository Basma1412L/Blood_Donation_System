This application is the backend of a blood donation system. The application allows donor to locatios of the donation centers that they can donate in and allow the managers to add appointments and add the donations to the system. 

There are two main roles:
1- Manager: Person who can:
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
    
2- Donor: Person who can:
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
7- to check the project locally before using heroku uncomment this line in the models.py module # database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME) and use the local database in the same way as we did in the testing
8- comment the line again and check heroku 
9- and never forget: flask run or python app.py to run the module 
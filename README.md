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
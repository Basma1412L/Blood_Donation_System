import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Database connection string
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'blood_donation_system')
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI='postgres://atyqejusvixadd:9aeeb8c28abcc0c4f5be39e6f93fea50f3e962f44b73ecfa6450260acb63289e@ec2-54-85-13-135.compute-1.amazonaws.com:5432/dclm7h9kc6hijf'
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
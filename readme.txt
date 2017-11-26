Medicate a better emergency logistics service for the ambulance and the hospital.

To run the project:

Install-flask,flask-sqlalchemy,flask-migrate,flask-bcrypt

Create database:
open mysql:
create database codle;

use commands:
python db.py db init
python db.py db migrate
python db.py db upgrade

Now run:
python run.py


The heart of this project contains an algorithm which normalises the various parameters to produce the best recommendation for the user.

from flask_db import db
from flask_db import app
from flask_db import User

users = User.query.all()

print users
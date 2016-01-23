from flask_db import db
from flask_db import app
from flask_db import User

admin = User('admafafdin', 'aaaindfasdfadsfadsafd')
guest = User('auefasdfst', 'aaestasdfadsfdsafdasd')

#print admin
#print guest

db.session.add(admin)
db.session.add(guest)

db.session.commit()
#file list 
##create.py
#dt_db.py

from dt_db import db
from dt_db import app
from dt_db import Post
from dt_db import Category

py = Category('Python')
p = Post('Hello Python!', 'Python is pretty cool', py)
db.session.add(py)
db.session.add(p)
db.session.commit()
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app import db 

class Question(db.Model) : 
    id = db.Column(db.Integer,primary_key=True)
    pass
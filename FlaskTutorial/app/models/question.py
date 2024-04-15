import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app import db 

class Question(db.Model) : 
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(200),nullable = False )
    content = db.Column(db.Text(),nullable=False)
    createDate = db.Column(db.DateTime(), nullable = False)

    
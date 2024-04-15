import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app import db 

# from models import question
class Answer(db.Model) :
    id = db.Collumn(db.Integer,primary_key=True)
    question_id = db.Column(db.Integer,db.Foreignkey('question.id',ondelte='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

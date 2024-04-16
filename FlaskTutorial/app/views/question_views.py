from flask import Blueprint,render_template,url_for,request
from app.models.Question import Question
from werkzeug.utils import redirect
from app.forms.questionForms import QuestionForms
from app.forms.answerForms import AnswerForm
from datetime import datetime
from app import db
bp = Blueprint('question',__name__,url_prefix='/question')

@bp.route('/list')
def list() :
    page = request.args.get('page', type=int, default=1)  # 페이지
    

    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template("/question_list.html",question_list= question_list)

@bp.route('/detail/<int:question_id>/')
def question_detail(question_id) : 
    forms= AnswerForm()
    detail_question = Question.query.get(question_id)
    return render_template("/question_detail.html",detail_question= detail_question,form=forms)

@bp.route('/create', methods=("POST","GET"))
def create():
    forms = QuestionForms()
    if request.method =="POST" and forms.validate_on_submit() : 
        question = Question(
            subject= forms.subject.data,
            content= forms.content.data,
            create_date = datetime.now()
            )
        db.session.add(question)
        db.session.commit()

        return redirect(url_for("question.question_detail",question_id= question.id))
    else : 
         return render_template("question_create.html", form = forms )
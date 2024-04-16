from flask import Flask,url_for,render_template,Blueprint,request
from app.models.Answer import Answer
from app.models.Question import Question
from app import db 
from datetime import datetime 
from werkzeug.utils import redirect
from app.forms.answerForms import AnswerForm
bp = Blueprint("answer",__name__,url_prefix=('/answer'))

@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id) :
    forms = AnswerForm()
    target_question = Question.query.get_or_404(question_id)
    if forms.validate_on_submit() : 
        content = request.form['content']
        answer = Answer(content= content, create_date= datetime.now(),question = target_question)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('question.question_detail',question_id=question_id))
    return render_template('question_detail.html', question=target_question, form=forms)
    
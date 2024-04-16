from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class AnswerForm(FlaskForm) : 
    content = TextAreaField('내용',validators=[DataRequired("제목은 필수 항목 입니다.")])
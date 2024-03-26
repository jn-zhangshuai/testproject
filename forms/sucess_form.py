from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class sucess_form(FlaskForm):
    prompt = StringField(label="问题:", validators=[DataRequired()])
    answer = TextAreaField(label="回答:", validators=None)
    submit = SubmitField(label="send")

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class adduser_form(FlaskForm):
    addusername = StringField(label="用户名:", validators=[DataRequired()])
    addpwd = StringField(label="密码:", validators=[DataRequired()])
    submit = SubmitField(label="add")
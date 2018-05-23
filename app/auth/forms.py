from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged In')
    submit = SubmitField('Log In')


class ClientForm(FlaskForm):
    nome = StringField('Nome:', validators=[DataRequired(), Length(6, 20)])
    idade = StringField('Idade :', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Cadastrar')


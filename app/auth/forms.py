from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
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

class ClienteForm(FlaskForm):
    cpfcnpj = IntegerField('CpfCnpj', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Gravar')

    def to_model(self, cliente):
        cliente.cpfcnpj = self.cpfcnpj.data
        cliente.nome = self.nome.data

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(6, 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.matricula = self.matricula.data
        funcionario.nome = self.nome.data
        funcionario.password = self.password.data

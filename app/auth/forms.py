from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email
from .. models import Cliente
import sqlite3


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
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    submit = SubmitField('Gravar')

    def to_model(self, cliente):
        cliente.cpfcnpj = self.cpfcnpj.data
        cliente.nome = self.nome.data

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.matricula = self.matricula.data
        funcionario.nome = self.nome.data
        funcionario.password = self.password.data

class AtividadeForm(FlaskForm):
    id = IntegerField('Cod atividade', validators=[DataRequired()])
    descricao = TextAreaField('Descrição:', validators=[DataRequired(), Length(6, 300)])
    submit = SubmitField('Gravar')

    def to_model(self, atividade):
        atividade.id = self.id.data
        atividade.descricao = self.descricao.data

class ProjetoForm(FlaskForm):
    id = IntegerField('Cod Projeto', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])

    conn = sqlite3.connect(("././data-dev.sqlite"))
    # This is the important part, here we are setting row_factory property of
    # connection object to sqlite3.Row(sqlite3.Row is an implementation of
    # row_factory)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select id, nome from cliente")
    lista = c.fetchall()
    if(lista == None):
        lista = [(1, "Nao Deu"), (2, "Nao Deu 2")]


    cliente_id = SelectField('Cliente:', choices= lista, coerce=int, validators=[DataRequired()])
    descricao = TextAreaField('Descricao:', validators=[DataRequired(), Length(6, 300)])
    submit = SubmitField('Gravar')

    def to_model(self, projeto):
        projeto.id = self.id.data
        projeto.nome = self.descricao.data
        projeto.cliente_id = self.cliente_id.data
        projeto.descricao = self.descricao.data






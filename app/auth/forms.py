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

    def to_form(self, cliente):
        self.cpfcnpj.data = cliente.cpfcnpj
        self.nome.data = cliente.nome

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.matricula = self.matricula.data
        funcionario.nome = self.nome.data
        funcionario.password = self.password.data

class EditarFuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.matricula = self.matricula.data
        funcionario.nome = self.nome.data

    def to_form(self, funcionario):
        self.matricula.data = funcionario.matricula
        self.nome.data = funcionario.nome


class AtividadeForm(FlaskForm):
    id = IntegerField('Cod atividade', validators=[DataRequired()])
    descricao = TextAreaField('Descrição:', validators=[DataRequired(), Length(6, 300)])
    submit = SubmitField('Gravar')

    def to_model(self, atividade):
        atividade.id = self.id.data
        atividade.descricao = self.descricao.data

    def to_form(self, atividade):
        self.id.data = atividade.id
        self.descricao.data = atividade.descricao

class ProjetoForm(FlaskForm):
    id = IntegerField('Cod Projeto', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])

    conn = sqlite3.connect(("././data-dev.sqlite"))
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
        projeto.nome = self.nome.data
        projeto.cliente_id = self.cliente_id.data
        projeto.descricao = self.descricao.data

    def to_form(self, projeto):
        self.id.data = projeto.id
        self.nome.data = projeto.nome
        self.cliente_id.data = projeto.cliente_id
        self.descricao.data = projeto.descricao

class FuncionarioProjetoForm(FlaskForm):
    id = IntegerField('Cod FuncionarioXPrjeto', validators=[DataRequired()])
    conn = sqlite3.connect(("././data-dev.sqlite"))
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select id, nome from funcionario")
    listaFuncionario = c.fetchall()
    funcionario_id = SelectField('Funcionario:', choices= listaFuncionario, coerce=int, validators=[DataRequired()])
    d = conn.cursor()
    d.execute("select id, nome from projeto")
    listaProjeto = d.fetchall()
    projeto_id = SelectField('Projeto:', choices=listaProjeto, coerce=int, validators=[DataRequired()])
    coordenador = BooleanField('Coordenador:')
    submit = SubmitField('Gravar')

    def to_model(self, funcionarioProjeto):
        funcionarioProjeto.id = self.id.data
        funcionarioProjeto.funcionario_id = self.funcionario_id.data
        funcionarioProjeto.projeto_id = self.projeto_id.data
        funcionarioProjeto.coordenador = self.coordenador.data

    def to_form(self, funcionarioProjeto):
        self.id.data = funcionarioProjeto.id
        self.funcionario_id.data = funcionarioProjeto.funcionario_id
        self.projeto_id.data = funcionarioProjeto.projeto_id  
        self.coordenador.data = funcionarioProjeto.coordenador





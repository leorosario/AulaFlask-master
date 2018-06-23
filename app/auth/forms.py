from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, PasswordField, BooleanField, SubmitField, SelectField, HiddenField, validators
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms_components import TimeField
from wtforms.fields.html5 import DateField
from .. models import Cliente
import sqlite3


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Mantenha-me conectado')
    submit = SubmitField('Logar')


class ClientForm(FlaskForm):
    nome = StringField('Nome:', validators=[DataRequired(), Length(6, 20)])
    idade = StringField('Idade :', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('Cadastrar')

class ClienteForm(FlaskForm):
    cpfcnpj = IntegerField('Cpf/Cnpj', validators=[DataRequired(), NumberRange(min=1, max=99999999999999, message="No maximo 14 digitos")])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    submit = SubmitField('Gravar')

    def to_model(self, cliente):
        cliente.cpfcnpj = self.cpfcnpj.data
        cliente.nome = self.nome.data

    def to_form(self, cliente):
        self.cpfcnpj.data = cliente.cpfcnpj
        self.nome.data = cliente.nome

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matrícula', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    email = StringField('E-mail:', validators=[DataRequired(), Length(2, 50)])
    password = PasswordField('Senha', validators=[DataRequired()])
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.matricula = self.matricula.data
        funcionario.nome = self.nome.data
        funcionario.email = self.email.data
        funcionario.password = self.password.data
        funcionario.is_admin = self.is_admin.data

class EditarFuncionarioForm(FlaskForm):
    matricula = IntegerField('Matrícula', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    email = StringField('E-mail:', validators=[DataRequired(), Length(2, 50)])
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.matricula = self.matricula.data
        funcionario.nome = self.nome.data
        funcionario.email = self.email.data
        funcionario.is_admin = self.is_admin.data

    def to_form(self, funcionario):
        self.matricula.data = funcionario.matricula
        self.nome.data = funcionario.nome
        self.email.data = funcionario.email
        self.is_admin.data = funcionario.is_admin


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
    id = IntegerField('Código Projeto', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired(), Length(2, 20)])
    cliente_id = SelectField('Cliente:', coerce=int, validators=[DataRequired()])
    descricao = TextAreaField('Descrição:', validators=[DataRequired(), Length(6, 300)])
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
    id = IntegerField('Código Funcionário X Projeto', validators=[DataRequired()])
    funcionario_id = SelectField('Funcionário:', coerce=int, validators=[DataRequired()])
    projeto_id = SelectField('Projeto:', coerce=int, validators=[DataRequired()])
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

class LancamentoForm(FlaskForm):
    projeto_id = SelectField('Projeto:', coerce=int, validators=[DataRequired()])
    dataInicio = DateField('Data Inicial', validators=[DataRequired()])
    horaInicio = TimeField('Hora Inicial',  validators=[DataRequired()])
    dataFim = DateField('Data Fim', validators=[DataRequired()])
    horaFim = TimeField('Hora Fim', validators=[DataRequired()])
    atividade_id = SelectField('Atividade:', coerce=int, validators=[DataRequired()])
    descricao = TextAreaField('Descrição:', validators=[DataRequired(), Length(6, 300)])
    submit = SubmitField('Gravar')

    def to_model(self, lancamento):
        lancamento.projeto_id = self.projeto_id.data
        lancamento.atividade_id = self.atividade_id.data
        lancamento.dataInicio = self.dataInicio.data
        lancamento.horaInicio = self.horaInicio.data
        lancamento.dataFim = self.dataFim.data
        lancamento.horaFim = self.horaFim.data
        lancamento.descricao = self.descricao.data

    def to_form(self, lancamento):
        self.projeto_id.data = lancamento.projeto_id
        self.atividade_id.data = lancamento.atividade_id
        self.dataInicio.data = lancamento.dataInicio
        self.horaInicio.data = lancamento.horaInicio
        self.dataFim.data = lancamento.dataFim
        self.horaFim.data = lancamento.horaFim
        self.descricao.data = lancamento.descricao

class AlterarSenhaForm(FlaskForm):
    passwordAtual = PasswordField('Senha Atual', validators=[DataRequired()])
    passwordNovo = PasswordField('Nova Senha', [validators.data_required(), validators.EqualTo('confirm', message='As senhas devem corresponder')])
    confirm = PasswordField('Repita Nova Senha', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def to_model(self, funcionario):
        funcionario.password = self.passwordNovo.data









from datetime import datetime
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(256))
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    bio = db.Column(db.Text)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(256))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    cpfcnpj = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)

class Funcionario(UserMixin, db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, nullable=False, unique=True)
    nome = db.Column(db.String(64), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Atividade(db.Model):
    __tablename__ = 'atividade'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(300), nullable=False)

class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    descricao = db.Column(db.String(300), nullable=False)

class FuncionarioProjeto(db.Model):
    __tablename__ = 'funcionarioProjeto'
    id = db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'))
    coordenador = db.Column(db.Boolean)

class Lancamento(db.Model):
    __tablename__ = 'lancamentos'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'))
    atividade_id = db.Column(db.Integer, db.ForeignKey('atividade.id'))
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
    dataInicio = db.Column(db.Date, nullable=False)
    horaInicio = db.Column(db.Time, nullable=False)
    dataFim = db.Column(db.Date, nullable=False)
    horaFim = db.Column(db.Time, nullable=False)
    descricao = db.Column(db.String(300), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return Funcionario.query.get(int(user_id))




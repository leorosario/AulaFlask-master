from datetime import datetime
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
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

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(256))

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



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




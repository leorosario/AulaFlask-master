
#!/usr/bin/env python
import os

from flask_migrate import Migrate, MigrateCommand

from app import create_app
from flask_script import Manager
from app import db
from app.models import User, Funcionario

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def adduser(email, nome, matricula, admin=True):
    """ Registra um novo usuário """
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt="Confirme: ")
    if password != password2:
        import sys
        sys.exit('Erro: senhas nao conferem')
    db.create_all()
    funcionario = Funcionario(email=email, nome=nome, matricula=matricula, password=password, is_admin=admin)
    db.session.add(funcionario)
    db.session.commit()
    print('Funcionario {0} foi registrado com sucesso.'.format(nome) )

if __name__ == '__main__':
    manager.run()



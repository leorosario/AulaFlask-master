from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from . import talks
from ..auth.forms import ClientForm
from ..auth.forms import ClienteForm
from ..auth.forms import FuncionarioForm
from ..models import User, Cliente, Funcionario

@talks.route('/')
def index():
    return render_template('talks/index.html')

@talks.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('talks/user.html', user=user)

@talks.route('/alterarSenha', methods = ['GET', 'POST'])
def alterarSenha():
    return render_template('/talks/alterarSenha.html')

@talks.route('/admin/atividades', methods = ['GET', 'POST'])
def atividades():
    return render_template('/talks/atividades.html')

@talks.route('/admin/clientes', methods = ['GET', 'POST'])
@login_required
def cadastrarCliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente()
        form.to_model(cliente)
        db.session.add(cliente)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('.index'))
    return render_template('/talks/cadastrarCliente.html', form = form)

@talks.route('/admin/funcionario', methods = ['GET', 'POST'])
@login_required
def cadastrarFuncionario():
    form = FuncionarioForm()
    if form.validate_on_submit():
        funcionario = Funcionario()
        form.to_model(funcionario)
        db.session.add(funcionario)
        db.session.commit()
        flash('Sucesso funcionario salvo.')
        return redirect(url_for('.index'))
    return render_template('/talks/cadastrarFuncionario.html', form = form)

@talks.route('/admin/projeto', methods = ['GET', 'POST'])
def cadastrarProjeto():
    return render_template('/talks/cadastrarProjeto.html')


@talks.route('/admin/vinculacao', methods = ['GET', 'POST'])
def vinculacao():
    return render_template('/talks/funcProjeto.html')

@talks.route('/home')
def home():
    return render_template('/talks/home.html')

@talks.route('/lancamento', methods = ['GET', 'POST'])
def lancamentoDeHorass():
    return render_template('/talks/lancamentoDeHoras.html')

@talks.route('/relatorios')
def relatorios():
    return render_template('/talks/relatorios.html')

@talks.route('/cliente', methods = ['GET', 'POST'])
def cliente():
    form = ClientForm()
    if form.validate_on_submit():
        flash('Nao deu')
        return redirect(url_for('.cliente'))
    return render_template('talks/cadastrarCliente.html', form=form)



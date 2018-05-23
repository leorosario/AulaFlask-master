from flask import render_template, redirect, url_for, flash
from . import talks
from ..auth.forms import ClientForm
from ..models import User

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
def cadastrarCliente():
    return render_template('/talks/cadastrarCliente.html')

@talks.route('/admin/funcionario', methods = ['GET', 'POST'])
def cadastrarFuncionario():
    return render_template('/talks/cadastrarFuncionario.html')

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



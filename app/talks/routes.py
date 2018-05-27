from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from . import talks
from ..auth.forms import ClientForm
from ..auth.forms import ClienteForm
from ..auth.forms import FuncionarioForm
from ..auth.forms import AtividadeForm
from ..auth.forms import ProjetoForm
from ..auth.forms import FuncionarioProjetoForm
from ..models import User, Cliente, Funcionario, Atividade,Projeto, FuncionarioProjeto

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
@login_required
def atividades():
    atividades = Atividade.query.all()
    return render_template('/talks/atividades.html', atividades = atividades)

@talks.route('/admin/atividades/cadastrar', methods = ['GET', 'POST'])
@login_required
def atividadesCadastrar():
    form = AtividadeForm()
    if form.validate_on_submit():
        atividade = Atividade()
        form.to_model(atividade)
        db.session.add(atividade)
        db.session.commit()
        flash('Sucesso atividade salva.')
        return redirect(url_for('talks.atividades'))
    return render_template('/talks/atividadesCadastrar.html', form = form)

@talks.route('/admin/clientes', methods = ['GET', 'POST'])
@login_required
def clientes():
    clientes = Cliente.query.all()
    return render_template('/talks/cliente.html', clientes = clientes)

@talks.route('/admin/clientes/cadastrar', methods = ['GET', 'POST'])
@login_required
def cadastrarCliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente()
        form.to_model(cliente)
        db.session.add(cliente)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('talks.cliente'))
    return render_template('/talks/cadastrarCliente.html', form = form)


@talks.route('/admin/funcionario', methods = ['GET', 'POST'])
@login_required
def funcionario():
    funcionarios = Funcionario.query.all()
    return render_template('/talks/funcionario.html', funcionarios = funcionarios)

@talks.route('/admin/funcionario/cadastrar', methods = ['GET', 'POST'])
@login_required
def cadastrarFuncionario():
    form = FuncionarioForm()
    if form.validate_on_submit():
        funcionario = Funcionario()
        form.to_model(funcionario)
        db.session.add(funcionario)
        db.session.commit()
        flash('Sucesso funcionario salvo.')
        return redirect(url_for('talks.funcionario'))
    return render_template('/talks/cadastrarFuncionario.html', form = form)

@talks.route('/admin/projeto', methods = ['GET', 'POST'])
def projeto():
    projetos = Projeto.query.all()
    for projeto in projetos:
        projeto.cliente = Cliente.query.get(projeto.cliente_id)
    return render_template('/talks/projeto.html', projetos = projetos)

@talks.route('/admin/projeto/cadastrar', methods = ['GET', 'POST'])
def cadastrarProjeto():
    form = ProjetoForm()
    if form.validate_on_submit():
        projeto = Projeto()
        form.to_model(projeto)
        db.session.add(projeto)
        db.session.commit()
        flash('Sucesso projeto salvo')
        return redirect(url_for('talks.projeto'))
    return render_template('/talks/cadastrarProjeto.html', form = form)


@talks.route('/admin/vinculacao', methods = ['GET', 'POST'])
def vinculacao():
    vinculacoes = FuncionarioProjeto.query.all()
    for vinculacao in vinculacoes:
        vinculacao.funcionario = Funcionario.query.get(vinculacao.funcionario_id)
        vinculacao.projeto = Projeto.query.get(vinculacao.projeto_id)
    return render_template('/talks/vinculacao.html', vinculacoes = vinculacoes)

@talks.route('/admin/vinculacao/cadastrar', methods = ['GET', 'POST'])
def vinculacaoCadastrar():
    form = FuncionarioProjetoForm()
    if form.validate_on_submit():
        funcionarioProjeto = FuncionarioProjeto()
        form.to_model(funcionarioProjeto)
        db.session.add(funcionarioProjeto)
        db.session.commit()
        flash('Sucesso funcionarioProjeto salvo')
        return redirect(url_for('talks.vinculacao'))
    return render_template('/talks/vinculacaoCadastrar.html', form = form)

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



from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from . import talks
from ..auth.forms import ClientForm
from ..auth.forms import ClienteForm
from ..auth.forms import FuncionarioForm
from ..auth.forms import EditarFuncionarioForm
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

@talks.route('/admin/atividades/editar/<int:id>', methods = ['GET', 'POST'])
@login_required
def atividadesEditar(id):
    atividade = Atividade.query.filter_by(id=id).first()
    form = AtividadeForm()
    if form.validate_on_submit():
        form.to_model(atividade)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('talks.atividades'))
    form.to_form(atividade)
    return render_template('/talks/atividadesEditar.html', form = form)

@talks.route('/admin/atividades/deletar/<int:id>', methods = ['GET', 'POST'])
@login_required
def atividadesDeletar(id):
    atividade = Atividade.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(atividade)
        db.session.commit()
        flash('Sucesso atividade deletada.')
        return redirect(url_for('talks.clientes'))
    return render_template('/talks/atividadesDeletar.html', atividade = atividade)

@talks.route('/admin/atividades/detalhes/<int:id>', methods = ['GET', 'POST'])
@login_required
def atividadesDetalhes(id):
    atividade = Atividade.query.filter_by(id=id).first()
    return render_template('/talks/atividadesDetalhes.html', atividade = atividade)

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
        return redirect(url_for('talks.clientes'))
    return render_template('/talks/clienteCadastrar.html', form = form)

@talks.route('/admin/clientes/editar/<int:id>', methods = ['GET', 'POST'])
@login_required
def editarCliente(id):
    cliente = Cliente.query.filter_by(id=id).first()
    form = ClienteForm()
    if form.validate_on_submit():
        form.to_model(cliente)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('talks.clientes'))
    form.to_form(cliente)
    return render_template('/talks/clienteEditar.html', form = form)

@talks.route('/admin/clientes/deletar/<int:id>', methods = ['GET', 'POST'])
@login_required
def deletarCliente(id):
    cliente = Cliente.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(cliente)
        db.session.commit()
        flash('Sucesso cliente deletado.')
        return redirect(url_for('talks.clientes'))
    return render_template('/talks/clienteDeletar.html', cliente = cliente)

@talks.route('/admin/clientes/detalhes/<int:id>', methods = ['GET', 'POST'])
@login_required
def detalhesCliente(id):
    cliente = Cliente.query.filter_by(id=id).first()
    return render_template('/talks/clienteDetalhes.html', cliente = cliente)

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
    return render_template('/talks/funcionarioCadastrar.html', form = form)

@talks.route('/admin/funcionario/editar/<int:id>', methods = ['GET', 'POST'])
@login_required
def editarFuncionario(id):
    funcionario = Funcionario.query.filter_by(id=id).first()
    form = EditarFuncionarioForm()
    if form.validate_on_submit():
        form.to_model(funcionario)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('talks.funcionario'))
    form.to_form(funcionario)
    return render_template('/talks/funcionarioEditar.html', form = form)

@talks.route('/admin/funcionario/deletar/<int:id>', methods = ['GET', 'POST'])
@login_required
def deletarFuncionario(id):
    funcionario = Funcionario.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(funcionario)
        db.session.commit()
        flash('Sucesso funcionario deletado.')
        return redirect(url_for('talks.funcionario'))
    return render_template('/talks/funcionarioDeletar.html', funcionario = funcionario)

@talks.route('/admin/funcionario/detalhes/<int:id>', methods = ['GET', 'POST'])
@login_required
def detalhesFuncionario(id):
    funcionario = Funcionario.query.filter_by(id=id).first()
    return render_template('/talks/funcionarioDetalhes.html', funcionario = funcionario)

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
    return render_template('/talks/projetoCadastrar.html', form = form)

@talks.route('/admin/projeto/editar/<int:id>', methods = ['GET', 'POST'])
def editarProjeto(id):
    projeto = Projeto.query.filter_by(id=id).first()
    form = ProjetoForm()
    if form.validate_on_submit():
        form.to_model(projeto)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('talks.projeto'))
    form.to_form(projeto)
    return render_template('/talks/projetoEditar.html', form = form)

@talks.route('/admin/projeto/deletar/<int:id>', methods = ['GET', 'POST'])
def deletarProjeto(id):
    projeto = Projeto.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(projeto)
        db.session.commit()
        flash('Sucesso projeto deletado.')
        return redirect(url_for('talks.projeto'))
    projeto.cliente = Cliente.query.get(projeto.cliente_id)
    return render_template('/talks/projetoDeletar.html', projeto = projeto)

@talks.route('/admin/projeto/detalhes/<int:id>', methods = ['GET', 'POST'])
def detalhesProjeto(id):
    projeto = Projeto.query.filter_by(id=id).first()
    projeto.cliente = Cliente.query.get(projeto.cliente_id)
    return render_template('/talks/projetoDetalhes.html', projeto = projeto)

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
        flash('Sucesso vinculacao salva')
        return redirect(url_for('talks.vinculacao'))
    return render_template('/talks/vinculacaoCadastrar.html', form = form)

@talks.route('/admin/vinculacao/editar/<int:id>', methods = ['GET', 'POST'])
def vinculacaoEditar(id):
    funcionarioProjeto = FuncionarioProjeto.query.filter_by(id=id).first()
    form = FuncionarioProjetoForm()
    if form.validate_on_submit():
        form.to_model(funcionarioProjeto)
        db.session.commit()
        flash('Sucesso vinculacao salva.')
        return redirect(url_for('talks.vinculacao'))
    form.to_form(funcionarioProjeto)
    return render_template('/talks/vinculacaoEditar.html', form = form)

@talks.route('/admin/vinculacao/deletar/<int:id>', methods = ['GET', 'POST'])
def vinculacaoDeletar(id):
    vinculacao = FuncionarioProjeto.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(vinculacao)
        db.session.commit()
        flash('Sucesso vinculacao deletada.')
        return redirect(url_for('talks.vinculacao'))
    vinculacao.funcionario = Funcionario.query.get(vinculacao.funcionario_id)
    vinculacao.projeto = Projeto.query.get(vinculacao.projeto_id)
    return render_template('/talks/vinculacaoDeletar.html', vinculacao = vinculacao)

@talks.route('/admin/vinculacao/detalhes/<int:id>', methods = ['GET', 'POST'])
def vinculacaoDetalhes(id):
    vinculacao = FuncionarioProjeto.query.filter_by(id=id).first()
    vinculacao.funcionario = Funcionario.query.get(vinculacao.funcionario_id)
    vinculacao.projeto = Projeto.query.get(vinculacao.projeto_id)
    return render_template('/talks/vinculacaoDetalhes.html', vinculacao = vinculacao)

@talks.route('/home')
def home():
    return render_template('/talks/home.html')

@talks.route('/lancamento', methods = ['GET', 'POST'])
def lancamentoDeHorass():
    return render_template('/talks/lancamentoDeHoras.html')

@talks.route('/relatorios')
def relatorios():
    return render_template('/talks/relatorios.html')

#@talks.route('/cliente', methods = ['GET', 'POST'])
#def cliente():
#    form = ClientForm()
#   if form.validate_on_submit():
#        flash('Nao deu')
#        return redirect(url_for('.cliente'))
#   return render_template('talks/cadastrarCliente.html', form=form)



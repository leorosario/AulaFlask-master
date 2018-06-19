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
from ..auth.forms import AlterarSenhaForm
from ..auth.forms import LancamentoForm
from ..models import User, Cliente, Funcionario, Atividade, Projeto, FuncionarioProjeto, Lancamento


@talks.route('/')
def index():
    return render_template('talks/home.html')


@talks.route('/user/<nome>')
def user(nome):
    user = Funcionario.query.filter_by(nome=nome).first_or_404()
    return render_template('talks/user.html', user=user)


@talks.route('/alterarSenha', methods=['GET', 'POST'])
def alterarSenha():
    funcionario = Funcionario.query.filter_by(email=current_user.email).first()
    form = AlterarSenhaForm()
    if form.validate_on_submit() and funcionario.verify_password(form.passwordAtual.data):
        form.to_model(funcionario)
        db.session.commit()
        flash('Sucesso cliente salvo.')
        return redirect(url_for('talks.atividades'))
    return render_template('/talks/alterarSenha.html', form=form)


@talks.route('/admin/atividades', methods=['GET', 'POST'])
@login_required
def atividades():
    if current_user.is_admin:
        atividades = Atividade.query.all()
        return render_template('/talks/atividades.html', atividades=atividades)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/atividades/cadastrar', methods=['GET', 'POST'])
@login_required
def atividadesCadastrar():
    if current_user.is_admin:
        form = AtividadeForm()
        if form.validate_on_submit():
            atividade = Atividade()
            form.to_model(atividade)
            db.session.add(atividade)
            db.session.commit()
            flash('Sucesso atividade salva.')
            return redirect(url_for('talks.atividades'))
        return render_template('/talks/atividadesCadastrar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/atividades/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def atividadesEditar(id):
    if current_user.is_admin:
        atividade = Atividade.query.filter_by(id=id).first()
        form = AtividadeForm()
        if form.validate_on_submit():
            form.to_model(atividade)
            db.session.commit()
            flash('Sucesso atividade salvo.')
            return redirect(url_for('talks.atividades'))
        form.to_form(atividade)
        return render_template('/talks/atividadesEditar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/atividades/deletar/<int:id>', methods=['GET', 'POST'])
@login_required
def atividadesDeletar(id):
    if current_user.is_admin:
        atividade = Atividade.query.filter_by(id=id).first()
        if request.method == "POST":
            db.session.delete(atividade)
            db.session.commit()
            flash('Sucesso atividade deletada.')
            return redirect(url_for('talks.clientes'))
        return render_template('/talks/atividadesDeletar.html', atividade=atividade)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/atividades/detalhes/<int:id>', methods=['GET', 'POST'])
@login_required
def atividadesDetalhes(id):
    if current_user.is_admin:
        atividade = Atividade.query.filter_by(id=id).first()
        return render_template('/talks/atividadesDetalhes.html', atividade=atividade)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/clientes', methods=['GET', 'POST'])
@login_required
def clientes():
    if current_user.is_admin:
        clientes = Cliente.query.all()
        return render_template('/talks/cliente.html', clientes=clientes)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/clientes/cadastrar', methods=['GET', 'POST'])
@login_required
def cadastrarCliente():
    if current_user.is_admin:
        form = ClienteForm()
        if form.validate_on_submit():
            cliente = Cliente()
            form.to_model(cliente)
            db.session.add(cliente)
            db.session.commit()
            flash('Sucesso cliente salvo.')
            return redirect(url_for('talks.clientes'))
        return render_template('/talks/clienteCadastrar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/clientes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editarCliente(id):
    if current_user.is_admin:
        cliente = Cliente.query.filter_by(id=id).first()
        form = ClienteForm()
        if form.validate_on_submit():
            form.to_model(cliente)
            db.session.commit()
            flash('Sucesso cliente salvo.')
            return redirect(url_for('talks.clientes'))
        form.to_form(cliente)
        return render_template('/talks/clienteEditar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/clientes/deletar/<int:id>', methods=['GET', 'POST'])
@login_required
def deletarCliente(id):
    if current_user.is_admin:
        cliente = Cliente.query.filter_by(id=id).first()
        if request.method == "POST":
            db.session.delete(cliente)
            db.session.commit()
            flash('Sucesso cliente deletado.')
            return redirect(url_for('talks.clientes'))
        return render_template('/talks/clienteDeletar.html', cliente=cliente)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/clientes/detalhes/<int:id>', methods=['GET', 'POST'])
@login_required
def detalhesCliente(id):
    if current_user.is_admin:
        cliente = Cliente.query.filter_by(id=id).first()
        return render_template('/talks/clienteDetalhes.html', cliente=cliente)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/funcionario', methods=['GET', 'POST'])
@login_required
def funcionario():
    if current_user.is_admin:
        funcionarios = Funcionario.query.all()
        return render_template('/talks/funcionario.html', funcionarios=funcionarios)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/funcionario/cadastrar', methods=['GET', 'POST'])
@login_required
def cadastrarFuncionario():
    if current_user.is_admin:
        form = FuncionarioForm()
        if form.validate_on_submit():
            funcionario = Funcionario()
            form.to_model(funcionario)
            db.session.add(funcionario)
            db.session.commit()
            flash('Sucesso funcionario salvo.')
            return redirect(url_for('talks.funcionario'))
        return render_template('/talks/funcionarioCadastrar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/funcionario/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editarFuncionario(id):
    if current_user.is_admin:
        funcionario = Funcionario.query.filter_by(id=id).first()
        form = EditarFuncionarioForm()
        if form.validate_on_submit():
            form.to_model(funcionario)
            db.session.commit()
            flash('Sucesso cliente salvo.')
            return redirect(url_for('talks.funcionario'))
        form.to_form(funcionario)
        return render_template('/talks/funcionarioEditar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/funcionario/deletar/<int:id>', methods=['GET', 'POST'])
@login_required
def deletarFuncionario(id):
    if current_user.is_admin:
        funcionario = Funcionario.query.filter_by(id=id).first()
        if request.method == "POST":
            db.session.delete(funcionario)
            db.session.commit()
            flash('Sucesso funcionario deletado.')
            return redirect(url_for('talks.funcionario'))
        return render_template('/talks/funcionarioDeletar.html', funcionario=funcionario)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/funcionario/detalhes/<int:id>', methods=['GET', 'POST'])
@login_required
def detalhesFuncionario(id):
    if current_user.is_admin:
        funcionario = Funcionario.query.filter_by(id=id).first()
        return render_template('/talks/funcionarioDetalhes.html', funcionario=funcionario)
    else:
        return render_template('/talks/notAdmin.html')
    


@talks.route('/admin/projeto', methods=['GET', 'POST'])
def projeto():
    if current_user.is_admin:
        projetos = Projeto.query.all()
        for projeto in projetos:
            projeto.cliente = Cliente.query.get(projeto.cliente_id)
        return render_template('/talks/projeto.html', projetos=projetos)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/projeto/cadastrar', methods=['GET', 'POST'])
def cadastrarProjeto():
    if current_user.is_admin:
        form = ProjetoForm()
        form.cliente_id.choices = [(cliente.id, cliente.nome)
                               for cliente in Cliente.query.all()]
        if form.validate_on_submit():
            projeto = Projeto()
            form.to_model(projeto)
            db.session.add(projeto)
            db.session.commit()
            flash('Sucesso projeto salvo')
            return redirect(url_for('talks.projeto'))
        return render_template('/talks/projetoCadastrar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/projeto/editar/<int:id>', methods=['GET', 'POST'])
def editarProjeto(id):
    if current_user.is_admin:
        projeto = Projeto.query.filter_by(id=id).first()
        form = ProjetoForm()
        form.cliente_id.choices = [(cliente.id, cliente.nome)
                               for cliente in Cliente.query.all()]
        if form.validate_on_submit():
            form.to_model(projeto)
            db.session.commit()
            flash('Sucesso cliente salvo.')
            return redirect(url_for('talks.projeto'))
        form.to_form(projeto)
        return render_template('/talks/projetoEditar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/projeto/deletar/<int:id>', methods=['GET', 'POST'])
def deletarProjeto(id):
    if current_user.is_admin:
        projeto = Projeto.query.filter_by(id=id).first()
        if request.method == "POST":
            db.session.delete(projeto)
            db.session.commit()
            flash('Sucesso projeto deletado.')
            return redirect(url_for('talks.projeto'))
        projeto.cliente = Cliente.query.get(projeto.cliente_id)
        return render_template('/talks/projetoDeletar.html', projeto=projeto)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/projeto/detalhes/<int:id>', methods=['GET', 'POST'])
def detalhesProjeto(id):
    if current_user.is_admin:
        projeto = Projeto.query.filter_by(id=id).first()
        projeto.cliente = Cliente.query.get(projeto.cliente_id)
        return render_template('/talks/projetoDetalhes.html', projeto=projeto)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/vinculacao', methods=['GET', 'POST'])
def vinculacao():
    if current_user.is_admin:
        vinculacoes = FuncionarioProjeto.query.all()
        for vinculacao in vinculacoes:
            vinculacao.funcionario = Funcionario.query.get(vinculacao.funcionario_id)
            vinculacao.projeto = Projeto.query.get(vinculacao.projeto_id)
        return render_template('/talks/vinculacao.html', vinculacoes=vinculacoes)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/vinculacao/cadastrar', methods=['GET', 'POST'])
def vinculacaoCadastrar():
    if current_user.is_admin:
        form = FuncionarioProjetoForm()
        form.funcionario_id.choices = [
            (funcionario.id, funcionario.nome) for funcionario in Funcionario.query.all()]
        form.projeto_id.choices = [(projeto.id, projeto.nome)
                               for projeto in Projeto.query.all()]
        if form.validate_on_submit():
            funcionarioProjeto = FuncionarioProjeto()
            form.to_model(funcionarioProjeto)
            db.session.add(funcionarioProjeto)
            db.session.commit()
            flash('Sucesso vinculacao salva')
            return redirect(url_for('talks.vinculacao'))
        return render_template('/talks/vinculacaoCadastrar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/vinculacao/editar/<int:id>', methods=['GET', 'POST'])
def vinculacaoEditar(id):
    if current_user.is_admin:
        funcionarioProjeto = FuncionarioProjeto.query.filter_by(id=id).first()
        form = FuncionarioProjetoForm()
        form.funcionario_id.choices = [
            (funcionario.id, funcionario.nome) for funcionario in Funcionario.query.all()]
        form.projeto_id.choices = [(projeto.id, projeto.nome)
                               for projeto in Projeto.query.all()]
        if form.validate_on_submit():
            form.to_model(funcionarioProjeto)
            db.session.commit()
            flash('Sucesso vinculacao salva.')
            return redirect(url_for('talks.vinculacao'))
        form.to_form(funcionarioProjeto)
        return render_template('/talks/vinculacaoEditar.html', form=form)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/vinculacao/deletar/<int:id>', methods=['GET', 'POST'])
def vinculacaoDeletar(id):
    if current_user.is_admin:
        vinculacao = FuncionarioProjeto.query.filter_by(id=id).first()
        if request.method == "POST":
            db.session.delete(vinculacao)
            db.session.commit()
            flash('Sucesso vinculacao deletada.')
            return redirect(url_for('talks.vinculacao'))
        vinculacao.funcionario = Funcionario.query.get(vinculacao.funcionario_id)
        vinculacao.projeto = Projeto.query.get(vinculacao.projeto_id)
        return render_template('/talks/vinculacaoDeletar.html', vinculacao=vinculacao)
    else:
        return render_template('/talks/notAdmin.html')


@talks.route('/admin/vinculacao/detalhes/<int:id>', methods=['GET', 'POST'])
def vinculacaoDetalhes(id):
    if current_user.is_admin:
        vinculacao = FuncionarioProjeto.query.filter_by(id=id).first()
        vinculacao.funcionario = Funcionario.query.get(vinculacao.funcionario_id)
        vinculacao.projeto = Projeto.query.get(vinculacao.projeto_id)
        return render_template('/talks/vinculacaoDetalhes.html', vinculacao=vinculacao)
    else:
        return render_template('/talks/notAdmin.html')

@talks.route('/lancamento', methods=['GET', 'POST'])
@login_required
def lancamento():
    lancamentos = Lancamento.query.all()
    for lancamento in lancamentos:
        lancamento.funcionario = Funcionario.query.get(lancamento.funcionario_id)
        lancamento.projeto = Projeto.query.get(lancamento.projeto_id)
        lancamento.atividade = Atividade.query.get(lancamento.atividade_id)
    return render_template('/talks/lancamento.html', lancamentos=lancamentos)

@talks.route('/lancamento/cadastrar', methods=['GET', 'POST'])
@login_required
def lancamentoCadastrar():
    form = LancamentoForm()
    form.projeto_id.choices = [(projeto.id, projeto.nome) for projeto in Projeto.query.all()]
    form.atividade_id.choices = [(atividade.id, atividade.descricao) for atividade in Atividade.query.all()]
    if form.validate_on_submit():
        lancamento = Lancamento()
        form.to_model(lancamento)
        lancamento.funcionario_id = current_user.id
        db.session.add(lancamento)
        db.session.commit()
        flash('Sucesso lancamento salvo')
        return redirect(url_for('talks.home'))
    return render_template('/talks/lancamentoCadastrar.html', form=form)

@talks.route('/lancamentoAjax', methods=['GET', 'POST'])
@login_required
def lancamentoAjax():
    obj = request.json;
    form = LancamentoForm;
    form.to_form(obj);
    lancamento = Lancamento()
    form.to_model(lancamento)
    lancamento.funcionario_id = current_user.id
    db.session.add(lancamento)
    db.session.commit()
    return redirect(url_for('talks.home'))

@talks.route('/lancamento/editar/<int:id>', methods=['GET', 'POST'])
def lancamentoEditar(id):
    lancamento = Lancamento.query.filter_by(id=id).first()
    form = LancamentoForm()
    form.projeto_id.choices = [(projeto.id, projeto.nome) for projeto in Projeto.query.all()]
    form.atividade_id.choices = [(atividade.id, atividade.descricao) for atividade in Atividade.query.all()]
    if form.validate_on_submit():
        form.to_model(lancamento)
        db.session.commit()
        flash('Sucesso lancamento salvo.')
        return redirect(url_for('talks.lancamento'))
    form.to_form(lancamento)
    return render_template('/talks/lancamentoEditar.html', form=form)

@talks.route('/lancamento/deletar/<int:id>', methods=['GET', 'POST'])
def lancamentoDeletar(id):
    lancamento = Lancamento.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(lancamento)
        db.session.commit()
        flash('Sucessolancamento deletado.')
        return redirect(url_for('talks.lancamento'))
    lancamento.atividade = Atividade.query.get(lancamento.atividade_id)
    lancamento.projeto = Projeto.query.get(lancamento.projeto_id)
    lancamento.funcionario = Funcionario.query.get(lancamento.funcionario_id)
    return render_template('/talks/lancamentoDeletar.html', lancamento=lancamento)

@talks.route('/lancamento/detalhes/<int:id>', methods=['GET', 'POST'])
def lancamentoDetalhes(id):
        lancamento = Lancamento.query.filter_by(id=id).first()
        lancamento.funcionario = Funcionario.query.get(lancamento.funcionario_id)
        lancamento.atividade = Atividade.query.get(lancamento.atividade_id)
        lancamento.projeto = Projeto.query.get(lancamento.projeto_id)
        return render_template('/talks/lancamentoDetalhes.html', lancamento=lancamento)

@talks.route('/home')
def home():
    return render_template('/talks/home.html')

@talks.route('/relatorios')
def relatorios():
    return render_template('/talks/relatorios.html')

# @talks.route('/cliente', methods = ['GET', 'POST'])
# def cliente():
#    form = ClientForm()
#   if form.validate_on_submit():
#        flash('Nao deu')
#        return redirect(url_for('.cliente'))
#   return render_template('talks/cadastrarCliente.html', form=form)

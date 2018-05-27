"""empty message

Revision ID: 1ecf01f03a12
Revises: 
Create Date: 2018-05-27 13:17:41.006860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ecf01f03a12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atividade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpfcnpj', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funcionario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricula', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('projeto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('descricao', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funcionarioProjeto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('funcionario_id', sa.Integer(), nullable=True),
    sa.Column('projeto_id', sa.Integer(), nullable=True),
    sa.Column('coordenador', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionarioProjeto')
    op.drop_table('projeto')
    op.drop_table('funcionario')
    op.drop_table('cliente')
    op.drop_table('atividade')
    # ### end Alembic commands ###
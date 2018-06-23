"""empty message

Revision ID: fc5d18323ba3
Revises: 
Create Date: 2018-06-23 11:20:56.306877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc5d18323ba3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lancamentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('projeto_id', sa.Integer(), nullable=True),
    sa.Column('atividade_id', sa.Integer(), nullable=True),
    sa.Column('funcionario_id', sa.Integer(), nullable=True),
    sa.Column('dataInicio', sa.Date(), nullable=False),
    sa.Column('horaInicio', sa.Time(), nullable=False),
    sa.Column('dataFim', sa.Date(), nullable=False),
    sa.Column('horaFim', sa.Time(), nullable=False),
    sa.Column('horasTrabalhadas', sa.Float(), nullable=False),
    sa.Column('descricao', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['atividade_id'], ['atividade.id'], ),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lancamentos')
    # ### end Alembic commands ###
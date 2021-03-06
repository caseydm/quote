"""empty message

Revision ID: 7923d1c19624
Revises: 12e7d56c5b75
Create Date: 2017-01-16 14:50:47.013780

"""

# revision identifiers, used by Alembic.
revision = '7923d1c19624'
down_revision = '12e7d56c5b75'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estimates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estimate_number', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('terms', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('tax_rate', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('line_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_estimate_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('rate', sa.Numeric(precision=8, scale=2), nullable=False),
    sa.Column('qty', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_estimate_id'], ['estimates.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('line_items')
    op.drop_table('estimates')
    ### end Alembic commands ###

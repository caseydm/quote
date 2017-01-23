"""empty message

Revision ID: 2589701d865d
Revises: 24d6686df8e8
Create Date: 2017-01-18 09:41:13.463737

"""

# revision identifiers, used by Alembic.
revision = '2589701d865d'
down_revision = '24d6686df8e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('estimates', sa.Column('sub_total', sa.Numeric(precision=8, scale=2), nullable=False))
    op.add_column('estimates', sa.Column('tax_total', sa.Numeric(precision=8, scale=2), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('estimates', 'tax_total')
    op.drop_column('estimates', 'sub_total')
    ### end Alembic commands ###
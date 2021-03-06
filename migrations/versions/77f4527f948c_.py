"""empty message

Revision ID: 77f4527f948c
Revises: 96b5f618f19b
Create Date: 2017-01-16 21:27:28.981616

"""

# revision identifiers, used by Alembic.
revision = '77f4527f948c'
down_revision = '96b5f618f19b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('estimates', sa.Column('date_of_issue', sa.DateTime(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('estimates', 'date_of_issue')
    ### end Alembic commands ###

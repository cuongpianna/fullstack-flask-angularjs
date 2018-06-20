"""empty message

Revision ID: a43e78464d18
Revises: ef3ba564673e
Create Date: 2018-06-08 11:17:26.018912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a43e78464d18'
down_revision = 'ef3ba564673e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('timestamp', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'timestamp')
    # ### end Alembic commands ###
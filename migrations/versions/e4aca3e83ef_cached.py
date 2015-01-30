"""add Page caching

Revision ID: e4aca3e83ef
Revises: 28ac33cbeede
Create Date: 2015-01-30 17:11:13.812731

"""

# revision identifiers, used by Alembic.
revision = 'e4aca3e83ef'
down_revision = '28ac33cbeede'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('preview', sa.Binary(), nullable=True))
    op.add_column('page', sa.Column('thumbnail', sa.Binary(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('page', 'thumbnail')
    op.drop_column('page', 'preview')
    ### end Alembic commands ###

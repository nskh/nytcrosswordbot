"""added lame count to user

Revision ID: 36a43ecd70b2
Revises: 898e5d8bc52c
Create Date: 2019-12-24 22:43:45.982515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a43ecd70b2'
down_revision = '898e5d8bc52c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lame_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lame_count')
    # ### end Alembic commands ###

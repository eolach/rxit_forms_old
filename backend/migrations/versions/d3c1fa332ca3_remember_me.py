"""remember-me

Revision ID: d3c1fa332ca3
Revises: f047e172122b
Create Date: 2018-08-19 15:28:43.626727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3c1fa332ca3'
down_revision = 'f047e172122b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('remember_me', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'remember_me')
    # ### end Alembic commands ###
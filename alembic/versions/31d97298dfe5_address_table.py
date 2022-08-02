"""address table

Revision ID: 31d97298dfe5
Revises: 
Create Date: 2022-08-01 15:47:40.393186

"""
from alembic import op
import sqlalchemy as sa
import app


# revision identifiers, used by Alembic.
revision = '31d97298dfe5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('districts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('districts')
    # ### end Alembic commands ###

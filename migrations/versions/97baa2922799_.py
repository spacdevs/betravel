"""empty message

Revision ID: 97baa2922799
Revises: cf59f0898098
Create Date: 2022-08-08 15:58:55.026730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97baa2922799'
down_revision = 'cf59f0898098'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('image_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'image_name')
    # ### end Alembic commands ###

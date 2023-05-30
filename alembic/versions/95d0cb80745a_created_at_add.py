"""created_at add

Revision ID: 95d0cb80745a
Revises: 47ae15b8949a
Create Date: 2023-05-29 14:04:05.389276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95d0cb80745a'
down_revision = '47ae15b8949a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('general_loc_data', sa.Column('created_at', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('general_loc_data', 'created_at')
    # ### end Alembic commands ###

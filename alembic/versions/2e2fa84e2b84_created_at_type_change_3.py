"""created_at type change 3

Revision ID: 2e2fa84e2b84
Revises: 5f2c0288aa24
Create Date: 2023-05-29 13:49:31.076827

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "2e2fa84e2b84"
down_revision = "5f2c0288aa24"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column(
    #     "general_loc_data",
    #     "created_at",
    #     existing_type=postgresql.TIMESTAMP(),
    #     type_=sa.Integer(),
    #     existing_nullable=True,
    # )
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column(
    #     "general_loc_data",
    #     "created_at",
    #     existing_type=sa.Integer(),
    #     type_=postgresql.TIMESTAMP(),
    #     existing_nullable=True,
    # )
    pass
    # ### end Alembic commands ###

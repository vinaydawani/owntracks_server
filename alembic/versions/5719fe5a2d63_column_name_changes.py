"""column name changes

Revision ID: 5719fe5a2d63
Revises: 76cb59adf300
Create Date: 2023-05-29 12:22:28.054020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5719fe5a2d63'
down_revision = '76cb59adf300'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('general_loc_data', sa.Column('acc', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('alt', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('batt', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('bs', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('cog', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('lat', sa.Double(), nullable=True))
    op.add_column('general_loc_data', sa.Column('lon', sa.Double(), nullable=True))
    op.add_column('general_loc_data', sa.Column('rad', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('t', sa.String(length=2), nullable=True))
    op.add_column('general_loc_data', sa.Column('tid', sa.String(), nullable=True))
    op.add_column('general_loc_data', sa.Column('tst', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('vac', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('vel', sa.Integer(), nullable=True))
    op.add_column('general_loc_data', sa.Column('p', sa.Float(), nullable=True))
    op.add_column('general_loc_data', sa.Column('poi', sa.String(), nullable=True))
    op.add_column('general_loc_data', sa.Column('m', sa.Integer(), nullable=True))
    op.drop_column('general_loc_data', 'battery_per')
    op.drop_column('general_loc_data', 'barometric_pressure_kpa')
    op.drop_column('general_loc_data', 'timestamp')
    op.drop_column('general_loc_data', 'monitoring_mode')
    op.drop_column('general_loc_data', 'latitude')
    op.drop_column('general_loc_data', 'tracker_id')
    op.drop_column('general_loc_data', 'accuracy_m')
    op.drop_column('general_loc_data', 'radius_m')
    op.drop_column('general_loc_data', 'altitude_m')
    op.drop_column('general_loc_data', 'velocity_kmh')
    op.drop_column('general_loc_data', 'vertical_accuracy_m')
    op.drop_column('general_loc_data', 'poi_name')
    op.drop_column('general_loc_data', 'course_over_ground')
    op.drop_column('general_loc_data', 'longitude')
    op.drop_column('general_loc_data', 'battery_status')
    op.drop_column('general_loc_data', 'trigger')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('general_loc_data', sa.Column('trigger', sa.VARCHAR(length=2), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('battery_status', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('longitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('course_over_ground', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('poi_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('vertical_accuracy_m', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('velocity_kmh', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('altitude_m', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('radius_m', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('accuracy_m', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('tracker_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('latitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('monitoring_mode', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('timestamp', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('barometric_pressure_kpa', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('general_loc_data', sa.Column('battery_per', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('general_loc_data', 'm')
    op.drop_column('general_loc_data', 'poi')
    op.drop_column('general_loc_data', 'p')
    op.drop_column('general_loc_data', 'vel')
    op.drop_column('general_loc_data', 'vac')
    op.drop_column('general_loc_data', 'tst')
    op.drop_column('general_loc_data', 'tid')
    op.drop_column('general_loc_data', 't')
    op.drop_column('general_loc_data', 'rad')
    op.drop_column('general_loc_data', 'lon')
    op.drop_column('general_loc_data', 'lat')
    op.drop_column('general_loc_data', 'cog')
    op.drop_column('general_loc_data', 'bs')
    op.drop_column('general_loc_data', 'batt')
    op.drop_column('general_loc_data', 'alt')
    op.drop_column('general_loc_data', 'acc')
    # ### end Alembic commands ###

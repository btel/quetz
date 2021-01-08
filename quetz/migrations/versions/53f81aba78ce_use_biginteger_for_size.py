"""use BigInteger for size

Revision ID: 53f81aba78ce
Revises: 30241b33d849
Create Date: 2021-01-08 22:09:48.268270

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '53f81aba78ce'
down_revision = '30241b33d849'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    if op.get_context().dialect.name == 'postgresql':
        op.alter_column(
            'channels',
            'size',
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
        op.alter_column(
            'channels',
            'size_limit',
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )

        op.alter_column(
            'package_versions',
            'size',
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    if op.get_context().dialect.name == 'postgresql':
        op.alter_column(
            'package_versions',
            'size',
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )

        op.alter_column(
            'channels',
            'size_limit',
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )
        op.alter_column(
            'channels',
            'size',
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )

    # ### end Alembic commands ###

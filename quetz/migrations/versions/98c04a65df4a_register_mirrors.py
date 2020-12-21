"""register mirrors

Revision ID: 98c04a65df4a
Revises: 8d1e9a9e0b1f
Create Date: 2020-12-21 11:10:15.107635

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '98c04a65df4a'
down_revision = '8d1e9a9e0b1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'channel_mirrors',
        sa.Column('id', sa.LargeBinary(length=16), nullable=False),
        sa.Column('channel_name', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('last_synchronised', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ['channel_name'],
            ['channels.name'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('url'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('channel_mirrors')
    # ### end Alembic commands ###

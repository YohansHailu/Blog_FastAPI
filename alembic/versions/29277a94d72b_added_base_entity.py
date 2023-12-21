"""added base entity

Revision ID: 29277a94d72b
Revises: c96ed0a44037
Create Date: 2023-12-21 13:29:14.241243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29277a94d72b'
down_revision: Union[str, None] = 'c96ed0a44037'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('userName', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('userName')
    )
    op.create_table('profile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('userId', sa.INTEGER(), nullable=True),
    sa.Column('firstName', sa.VARCHAR(), nullable=True),
    sa.Column('lastName', sa.VARCHAR(), nullable=True),
    sa.Column('bio', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('userId')
    )
    # ### end Alembic commands ###

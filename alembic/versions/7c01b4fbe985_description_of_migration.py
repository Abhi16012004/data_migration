"""Description of migration

Revision ID: 7c01b4fbe985
Revises: 11cec1d6c9df
Create Date: 2024-05-16 13:21:02.087973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c01b4fbe985'
down_revision: Union[str, None] = '11cec1d6c9df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mymodel', 'address')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mymodel', sa.Column('address', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
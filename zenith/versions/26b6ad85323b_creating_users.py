"""creating users

Revision ID: 26b6ad85323b
Revises: 
Create Date: 2024-04-19 22:26:06.315528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26b6ad85323b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users' , sa.Column('id' , sa.Integer(),nullable = False , primary_key=True),
                    sa.Column('email' , sa.String() , nullable = False , unique=True),
                    sa.Column('password' , sa.String() , nullable=False),
                    sa.Column('created_at' , sa.TIMESTAMP(timezone=True) , nullable = False,
                                           server_default= sa.text('NOW()')))


def downgrade() -> None:
    op.drop_table('users')

    


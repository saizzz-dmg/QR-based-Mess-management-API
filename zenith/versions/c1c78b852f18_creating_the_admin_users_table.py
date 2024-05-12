"""creating the admin users table

Revision ID: b13b00a97171
Revises: 26b6ad85323b
Create Date: 2024-04-19 22:48:42.807879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1c78b852f18'
down_revision: Union[str, None] = '26b6ad85323b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('adminUsers' , sa.Column('id' , sa.Integer(),nullable = False , primary_key=True),
                    sa.Column('email' , sa.String() , nullable = False , unique=True),
                    sa.Column('password' , sa.String() , nullable=False),
                    sa.Column('created_at' , sa.TIMESTAMP(timezone=True) , nullable = False,
                                           server_default= sa.text('NOW()')))
    


def downgrade() -> None:
    op.drop_table('adminUsers')


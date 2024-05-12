"""creating the cancellation table

Revision ID: aacb69d0bcec
Revises: c1c78b852f18
Create Date: 2024-05-02 18:13:54.779601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aacb69d0bcec'
down_revision: Union[str, None] = 'c1c78b852f18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('cancellation' , sa.Column('id' , sa.Integer(),primary_key= True , nullable = False),
                    sa.Column('user_email' , sa.String() , nullable = False),
                    sa.Column('start_date' , sa.Date , nullable = False),
                    sa.Column('end_date' , sa.Date , nullable = False))


def downgrade() -> None:
    op.drop_table('cancellation')





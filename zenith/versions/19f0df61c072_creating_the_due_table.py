"""creating the due table

Revision ID: 19f0df61c072
Revises: aacb69d0bcec
Create Date: 2024-05-09 01:46:29.358469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f0df61c072'
down_revision: Union[str, None] = 'aacb69d0bcec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('due_data' ,
                    sa.Column('user_email' , sa.String(),primary_key=True ,  nullable = False),
                    sa.Column('Cancel_month' , sa.Integer() ,primary_key= True, nullable = False),
                    sa.Column('cancel_days' , sa.Integer() , nullable=False),
                    sa.Column('paid' , sa.Boolean() , server_default='False' , nullable = False))
                    

def downgrade() -> None:
    op.drop_table('due_data')

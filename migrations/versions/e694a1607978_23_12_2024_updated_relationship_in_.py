"""23.12.2024 Updated relationship in Comment

Revision ID: e694a1607978
Revises: db6c945b5ab4
Create Date: 2024-12-23 15:24:29.892815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e694a1607978'
down_revision: Union[str, None] = 'db6c945b5ab4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
"""11.12.2024 Added age and bio fields in user model

Revision ID: 866a5149ff2f
Revises: 538e42a17838
Create Date: 2024-12-11 16:43:10.791155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '866a5149ff2f'
down_revision: Union[str, None] = '538e42a17838'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_id'), 'comment', ['id'], unique=False)
    op.add_column('user', sa.Column('bio', sa.String(length=2000), nullable=True))
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    op.drop_constraint('user_phone_number_key', 'user', type_='unique')
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.create_unique_constraint('user_phone_number_key', 'user', ['phone_number'])
    op.drop_column('user', 'age')
    op.drop_column('user', 'bio')
    op.drop_index(op.f('ix_comment_id'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###

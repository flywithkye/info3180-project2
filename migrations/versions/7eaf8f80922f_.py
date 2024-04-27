"""empty message

Revision ID: 7eaf8f80922f
Revises: 4dfb3d47338a
Create Date: 2024-04-26 20:23:32.979141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eaf8f80922f'
down_revision = '4dfb3d47338a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint('posts_user_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.create_unique_constraint('posts_user_id_key', ['user_id'])

    # ### end Alembic commands ###

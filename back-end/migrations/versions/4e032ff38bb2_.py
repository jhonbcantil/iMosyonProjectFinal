"""empty message

Revision ID: 4e032ff38bb2
Revises: 8c1241d2923c
Create Date: 2022-04-23 21:48:02.483596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4e032ff38bb2'
down_revision = '8c1241d2923c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users_predicted_words', 'predict_id',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users_predicted_words', 'predict_id',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###

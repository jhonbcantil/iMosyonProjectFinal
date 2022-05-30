"""empty message

Revision ID: 8c1241d2923c
Revises: cca72498e5d6
Create Date: 2022-04-23 21:45:37.984075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8c1241d2923c'
down_revision = 'cca72498e5d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_predicted_words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('predict_id', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('predict_id')
    )
    op.drop_constraint('predicted_word_ibfk_1', 'predicted_word', type_='foreignkey')
    op.drop_column('predicted_word', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('predicted_word', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('predicted_word_ibfk_1', 'predicted_word', 'user', ['user_id'], ['id'])
    op.drop_table('users_predicted_words')
    # ### end Alembic commands ###

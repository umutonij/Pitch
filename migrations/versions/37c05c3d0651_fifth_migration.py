"""fifth  Migration

Revision ID: 37c05c3d0651
Revises: 9af1e2f37cd9
Create Date: 2019-02-27 12:03:05.586049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c05c3d0651'
down_revision = '9af1e2f37cd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitches', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitches')
    op.add_column('comments', sa.Column('comment', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('username', sa.String(), nullable=True))
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitch', ['pitch_id'], ['id'])
    op.drop_column('comments', 'name')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'username')
    op.drop_column('comments', 'comment')
    op.create_table('pitches',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitches_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pitches_pkey')
    )
    op.drop_table('pitch')
    # ### end Alembic commands ###

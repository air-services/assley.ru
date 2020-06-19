"""Add seasons, episodes

Revision ID: fd3eac2b2030
Revises: 2d9ed7638712
Create Date: 2020-06-18 22:14:15.595908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd3eac2b2030'
down_revision = '2d9ed7638712'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('episodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('pages', sa.JSON(), nullable=True),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], ),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episodes')
    op.drop_table('seasons')
    # ### end Alembic commands ###

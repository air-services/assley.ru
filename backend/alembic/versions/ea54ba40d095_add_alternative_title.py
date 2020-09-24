"""Add alternative title

Revision ID: ea54ba40d095
Revises: d7474d86d422
Create Date: 2020-09-24 16:37:39.385503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea54ba40d095'
down_revision = 'd7474d86d422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('eng_title', sa.Unicode(), nullable=True))
    op.add_column('books', sa.Column('rus_title', sa.Unicode(), nullable=True))
    op.drop_column('books', 'title')
    op.create_foreign_key(None, 'books_authors', 'books', ['book_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'books_authors', 'authors', ['author_id'], ['id'])
    op.create_foreign_key(None, 'books_genres', 'genres', ['genre_id'], ['id'])
    op.create_foreign_key(None, 'books_genres', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'books_painters', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'books_painters', 'painters', ['painter_id'], ['id'])
    op.create_foreign_key(None, 'books_publishers', 'publishers', ['publisher_id'], ['id'])
    op.create_foreign_key(None, 'books_publishers', 'books', ['book_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'books_release_formates', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'books_sections', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'books_sections', 'sections', ['section_id'], ['id'])
    op.create_foreign_key(None, 'books_tags', 'books', ['book_id'], ['id'])
    op.create_foreign_key(None, 'books_tags', 'tags', ['tag_id'], ['id'])
    op.create_foreign_key(None, 'books_translators', 'translators', ['translator_id'], ['id'])
    op.create_foreign_key(None, 'books_translators', 'books', ['book_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books_translators', type_='foreignkey')
    op.drop_constraint(None, 'books_translators', type_='foreignkey')
    op.drop_constraint(None, 'books_tags', type_='foreignkey')
    op.drop_constraint(None, 'books_tags', type_='foreignkey')
    op.drop_constraint(None, 'books_sections', type_='foreignkey')
    op.drop_constraint(None, 'books_sections', type_='foreignkey')
    op.drop_constraint(None, 'books_release_formates', type_='foreignkey')
    op.drop_constraint(None, 'books_publishers', type_='foreignkey')
    op.drop_constraint(None, 'books_publishers', type_='foreignkey')
    op.drop_constraint(None, 'books_painters', type_='foreignkey')
    op.drop_constraint(None, 'books_painters', type_='foreignkey')
    op.drop_constraint(None, 'books_genres', type_='foreignkey')
    op.drop_constraint(None, 'books_genres', type_='foreignkey')
    op.drop_constraint(None, 'books_authors', type_='foreignkey')
    op.drop_constraint(None, 'books_authors', type_='foreignkey')
    op.add_column('books', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('books', 'rus_title')
    op.drop_column('books', 'eng_title')
    # ### end Alembic commands ###

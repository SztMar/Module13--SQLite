"""storage table and relation to book

Revision ID: b6d63f1bb9f5
Revises: 595f762766e3
Create Date: 2020-11-22 13:44:27.489101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6d63f1bb9f5'
down_revision = '595f762766e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loaned_date', sa.DateTime(), nullable=True),
    sa.Column('returned_date', sa.DateTime(), nullable=True),
    sa.Column('availability', sa.String(length=100), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_storage_availability'), 'storage', ['availability'], unique=False)
    op.create_index(op.f('ix_storage_loaned_date'), 'storage', ['loaned_date'], unique=False)
    op.create_index(op.f('ix_storage_returned_date'), 'storage', ['returned_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_storage_returned_date'), table_name='storage')
    op.drop_index(op.f('ix_storage_loaned_date'), table_name='storage')
    op.drop_index(op.f('ix_storage_availability'), table_name='storage')
    op.drop_table('storage')
    # ### end Alembic commands ###

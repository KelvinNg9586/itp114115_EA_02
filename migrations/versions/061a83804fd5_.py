"""empty message

Revision ID: 061a83804fd5
Revises: aca43b5ca196
Create Date: 2023-04-27 08:55:38.364951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '061a83804fd5'
down_revision = 'aca43b5ca196'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('orders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('status', sa.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('order_id', sa.INTEGER(), nullable=True),
    sa.Column('product_id', sa.INTEGER(), nullable=True),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

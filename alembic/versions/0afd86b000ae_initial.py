"""Initial

Revision ID: 0afd86b000ae
Revises: 
Create Date: 2021-04-07 18:28:35.220829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0afd86b000ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('admin_phones',
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admins.id'], ),
    sa.ForeignKeyConstraint(['phone_id'], ['phones.id'], )
    )
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('pwd_hash', sa.String(), nullable=False),
    sa.Column('primary_phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['primary_phone_id'], ['admin_phones.phone_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appliances_brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brand_name')
    )
    op.create_table('appliances_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type_name')
    )
    op.create_table('customer_phones',
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['phone_id'], ['phones.id'], )
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('primary_phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['primary_phone_id'], ['customer_phones.phone_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operator_phones',
    sa.Column('operator_id', sa.Integer(), nullable=True),
    sa.Column('phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operator_id'], ['operators.id'], ),
    sa.ForeignKeyConstraint(['phone_id'], ['phones.id'], )
    )
    op.create_table('operators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('pwd_hash', sa.String(), nullable=False),
    sa.Column('primary_phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['primary_phone_id'], ['operator_phones.phone_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('worker_phones',
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.Column('phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['phone_id'], ['phones.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], )
    )
    op.create_table('workers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('pwd_hash', sa.String(), nullable=False),
    sa.Column('primary_phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['primary_phone_id'], ['worker_phones.phone_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appliances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('appliances_name', sa.String(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['appliances_brand.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['appliances_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('appliances_name')
    )
    op.create_table('customer_addresses',
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], )
    )
    op.create_table('worker_appliances_types',
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['appliances_type.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], )
    )
    op.create_table('worker_brands',
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['appliances_brand.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], )
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.Column('appliances_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.ForeignKeyConstraint(['appliances_id'], ['appliances.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('worker_brands')
    op.drop_table('worker_appliances_types')
    op.drop_table('customer_addresses')
    op.drop_table('appliances')
    op.drop_table('workers')
    op.drop_table('worker_phones')
    op.drop_table('phones')
    op.drop_table('operators')
    op.drop_table('operator_phones')
    op.drop_table('customers')
    op.drop_table('customer_phones')
    op.drop_table('appliances_type')
    op.drop_table('appliances_brand')
    op.drop_table('admins')
    op.drop_table('admin_phones')
    op.drop_table('addresses')
    # ### end Alembic commands ###

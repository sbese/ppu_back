from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, Table, ForeignKey
from .database import Base

admin_phones = Table('admin_phones', Base.metadata,
                     Column('admin_id', Integer, ForeignKey('admins.id')),
                     Column('phone_id', Integer, ForeignKey('phones.id')))

operator_phones = Table('operator_phones', Base.metadata,
                        Column('operator_id', Integer, ForeignKey('operators.id')),
                        Column('phone_id', Integer, ForeignKey('phones.id')))

customer_phones = Table('customer_phones', Base.metadata,
                        Column('customer_id', Integer, ForeignKey('customers.id')),
                        Column('phone_id', Integer, ForeignKey('phones.id')))

worker_phones = Table('worker_phones', Base.metadata,
                      Column('worker_id', Integer, ForeignKey('workers.id')),
                      Column('phone_id', Integer, ForeignKey('phones.id'))
                      )

worker_brands = Table('worker_brands', Base.metadata,
                      Column('worker_id', Integer, ForeignKey('workers.id')),
                      Column('brand_id', Integer, ForeignKey('appliances_brand.id')))

worker_appliances_types = Table('worker_appliances_types', Base.metadata,
                                Column('worker_id', Integer, ForeignKey('workers.id')),
                                Column('brand_id', Integer, ForeignKey('appliances_type.id')))

customer_addresses = Table('customer_addresses', Base.metadata,
                           Column('customer_id', Integer, ForeignKey('customers.id')),
                           Column('address_id', Integer, ForeignKey('addresses.id')))


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    name = Column(String, nullable=True)
    pwd_hash = Column(String, nullable=False)

    # primary_phone_id = Column(Integer, ForeignKey('admin_phones.phone_id'))
    # primary_phone = relationship('Phone', back_populates="admins_primary")

    phones = relationship("Phone", secondary=admin_phones, )


class Operator(Base):
    __tablename__ = 'operators'
    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    name = Column(String, nullable=True)
    pwd_hash = Column(String, nullable=False)

    # primary_phone_id = Column(Integer, ForeignKey('operator_phones.phone_id'))
    # primary_phone = relationship('Phone', back_populates="operators_primary")

    phones = relationship("Phone", secondary=operator_phones)


class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    name = Column(String, nullable=True)
    pwd_hash = Column(String, nullable=False)

    # primary_phone_id = Column(Integer, ForeignKey('worker_phones.phone_id'))
    # primary_phone = relationship('Phone', back_populates="workers_primary")
    phones = relationship("Phone", secondary=worker_phones)

    appliances_brands = relationship('AppliancesBrand', secondary=worker_brands)
    appliances_types = relationship('AppliancesType', secondary=worker_appliances_types)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    # primary_phone_id = Column(Integer, ForeignKey('customer_phones.phone_id'))
    # primary_phone = relationship('Phone', back_populates="customers_primary")

    phones = relationship("Phone", secondary=customer_phones)
    addresses = relationship("Address", secondary=customer_addresses)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    worker_id = Column(Integer, ForeignKey('workers.id'))
    appliances_id = Column(Integer, ForeignKey('appliances.id'), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)

    appliances = relationship('Appliances')
    worker = relationship('Worker')
    customer = relationship('Customer')
    address = relationship('Address')

    status = Column(String, nullable=False)


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(Integer, unique=True)


class AppliancesBrand(Base):
    __tablename__ = 'appliances_brand'
    id = Column(Integer, primary_key=True)
    brand_name = Column(String, unique=True)


class AppliancesType(Base):
    __tablename__ = 'appliances_type'
    id = Column(Integer, primary_key=True)
    type_name = Column(String, unique=True)


class Appliances(Base):
    __tablename__ = 'appliances'
    id = Column(Integer, primary_key=True)
    appliances_name = Column(String, unique=True)

    brand_id = Column(Integer, ForeignKey('appliances_brand.id'))
    brand = relationship('AppliancesBrand')

    type_id = Column(Integer, ForeignKey('appliances_type.id'))
    appliances_type = relationship('AppliancesType')



class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

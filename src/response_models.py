from typing import List, ForwardRef

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    status: str = Field(default='ok')


class Phone(BaseModel):
    id: int
    phone: int


class Address(BaseModel):
    id: int
    name: str


class Admin(BaseModel):
    id: int
    login: str
    name: str
    primary_phone: int
    phones: List[Phone]


class Admins(BaseModel):
    items: List[Admin]


class Order(BaseModel):
    id: int

    customer_id: int
    customer_name: str
    customer_primary_phone: int

    worker_id: int
    worker_name: str
    worker_primary_phone: int

    appliances_id: int
    appliances_brand: str
    appliances_type: str

    address_id: int
    address_name: str

    status: str

class Orders(BaseModel):
    items: List[Order]

class Operator(BaseModel):
    id: int
    login: str
    name: str
    primary_phone: int
    phones: List[Phone]


class Operators(BaseModel):
    items: List[Operator]


class Worker(BaseModel):
    id: int
    login: str
    name: str
    primary_phone: int
    phones: List[Phone]
    orders: List[Order]


class Workers(BaseModel):
    items: List[Worker]


class Customer(BaseModel):
    id: int
    login: str
    name: str
    primary_phone: Phone
    phones: List[Phone]
    orders: List[Order]
    addresses: List[Address]

class Customers(BaseModel):
    items: List[Customer]


class AppliancesBrand(BaseModel):
    id: int
    brand_name: str

class AppliancesBrands(BaseModel):
    items: List[AppliancesBrand]


class AppliancesType(BaseModel):
    id: int
    type_name: str

class AppliancesTypes(BaseModel):
    items: List[AppliancesType]


class Appliances(BaseModel):
    id: int
    appliances_name: str
    brand: str
    appliances_type: str


class AppliancesList(BaseModel):
    items: List[Appliances]


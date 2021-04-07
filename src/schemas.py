from pydantic import BaseModel, Field
from typing import List


class LoginSchema(BaseModel):
    login: str
    pwd_hash: str


class CreateAdmin(BaseModel):
    login: str
    pwd_hash: str
    name: str
    phone: int


class CreateOperator(BaseModel):
    login: str
    pwd_hash: str
    name: str
    phone: int


class CreateWorker(BaseModel):
    login: str
    pwd_hash: str
    name: str
    phone: int


class CreateAppliancesBrand(BaseModel):
    brand_name: str


class CreateAppliancesType(BaseModel):
    type_name: str


class CreateAppliances(BaseModel):
    name: str
    brand_id: int
    appliances_type_id: int


class CreateCustomer(BaseModel):
    name: str
    phone: int


class CreateOrder(BaseModel):
    customer_id: int
    worker_id: int
    appliances_id: int

class NewPhone(BaseModel):
    new_phone: int

class NewName(BaseModel):
    new_name: str

class NewPassword(BaseModel):
    new_password: str
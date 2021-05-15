from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from .database import get_db

from . import response_models
from . import schemas
from . import models
app = FastAPI()


@app.post('/admin/login', response_model=response_models.BaseResponse, tags=['Администратор'])
def admin_login(login_data: schemas.LoginSchema, db: Session = Depends(get_db)):
    pass


@app.put('/admin/', response_model=response_models.BaseResponse, tags=['Администратор'])
def create_admin(new_admin: schemas.CreateAdmin, db: Session = Depends(get_db)):
    admin = models.Admin(
        login=new_admin.login,
        name=new_admin.name,
        pwd_hash=new_admin.pwd_hash,
    )
    db.add(admin)
    db.commit()
    return response_models.BaseResponse()

# , response_model=response_models.Admins
@app.get('/admins', tags=['Администратор'], response_model=response_models.Admins)
def get_admins(db: Session = Depends(get_db)):
    admins = db.query(models.Admin).all()
    return response_models.Admins(items=[
        response_models.Admin(
            id = x.id,
            name = x.name,
            login = x.login
        ) for x in admins
    ])



@app.get('/admin/{admin_id}', response_model=response_models.Admin, tags=['Администратор'])
def get_admins(admin_id: int, db: Session = Depends(get_db)):
    pass


@app.patch('/admin/{admin_id}/primary_phone', response_model=response_models.BaseResponse, tags=['Администратор'])
def change_admin_primary_phone(admin_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/admin/{admin_id}/phone', response_model=response_models.BaseResponse, tags=['Администратор'])
def add_admin_phone(admin_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/admin/{admin_id}/name', response_model=response_models.BaseResponse, tags=['Администратор'])
def change_admin_name(admin_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
    pass


@app.patch('/admin/{admin_id}/password', response_model=response_models.BaseResponse, tags=['Администратор'])
def change_admin_name(admin_id: int, new_password: schemas.NewPassword, db: Session = Depends(get_db)):
    pass


@app.delete('/admin/{admin_id}/phone', response_model=response_models.BaseResponse, tags=['Администратор'])
def remove_admin_phone(admin_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.put('/operator', response_model=response_models.BaseResponse, tags=['Оператор'])
def create_operator(new_operator: schemas.CreateOperator, db: Session = Depends(get_db)):
    pass


@app.get('/operators', response_model=response_models.Operators, tags=['Оператор'])
def get_operators(db: Session = Depends(get_db)):
    pass


@app.get('/operator/{operator_id}', response_model=response_models.Operator, tags=['Оператор'])
def get_operator(operator_id: int, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/primary_phone', response_model=response_models.BaseResponse, tags=['Оператор'])
def change_operator_primary_phone(operator_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/phone', response_model=response_models.BaseResponse, tags=['Оператор'])
def add_operator_phone(operator_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/name', response_model=response_models.BaseResponse, tags=['Оператор'])
def change_operator_name(operator_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/password', response_model=response_models.BaseResponse, tags=['Оператор'])
def change_operator_password(operator_id: int, new_password: schemas.NewPassword, db: Session = Depends(get_db)):
    pass


@app.delete('/operator/{operator_id}/phone', response_model=response_models.BaseResponse, tags=['Оператор'])
def remove_operator_phone(operator_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.put('/worker', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def create_worker(new_worker: schemas.CreateWorker, db: Session = Depends(get_db)):
    pass


@app.get('/workers', response_model=response_models.Workers, tags=['Исполнитель'])
def get_workers(db: Session = Depends(get_db)):
    pass


@app.get('/worker/{worker_id}', response_model=response_models.Worker, tags=['Исполнитель'])
def get_worker(worker_id: int, db: Session = Depends(get_db)):
    pass


@app.patch('/worker/{worker_id}/primary_phone', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def change_admin_primary_phone(worker_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/worker/{worker_id}/phone', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def add_worker_phone(worker_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/worker/{worker_id}/name', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def change_worker_name(worker_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
    pass


@app.patch('/worker/{worker_id}/password', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def change_worker_name(worker_id: int, new_password: schemas.NewPassword, db: Session = Depends(get_db)):
    pass


@app.delete('/worker/{worker_id}/phone', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def remove_worker_phone(worker_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.put('/appliances_brand', response_model=response_models.BaseResponse, tags=['Техника'])
def create_appliances_brand(new_appliances_brand: schemas.CreateAppliancesBrand, db: Session = Depends(get_db)):
    pass


@app.get('/appliances_brands', response_model=response_models.AppliancesBrands, tags=['Техника'])
def get_appliances_brands(db: Session = Depends(get_db)):
    pass


@app.put('/appliances_type', response_model=response_models.BaseResponse, tags=['Техника'])
def create_appliances_type(new_appliances_type: schemas.CreateAppliancesType, db: Session = Depends(get_db)):
    pass


@app.get('/appliances_types', response_model=response_models.AppliancesTypes, tags=['Техника'])
def get_appliances_types(db: Session = Depends(get_db)):
    pass


@app.put('/appliances', response_model=response_models.BaseResponse, tags=['Техника'])
def create_appliances(new_appliances: schemas.CreateAppliances, db: Session = Depends(get_db)):
    pass


@app.get('/appliances', response_model=response_models.AppliancesList, tags=['Техника'])
def get_appliances(db: Session = Depends(get_db)):
    pass


@app.put('/customer', response_model=response_models.BaseResponse, tags=['Клиент'])
def create_customer(new_customer: schemas.CreateCustomer, db: Session = Depends(get_db)):
    pass


@app.get('/customers', response_model=response_models.Customers, tags=['Клиент'])
def create_worker(db: Session = Depends(get_db)):
    pass


@app.get('/customer/{customer_id}', response_model=response_models.Customer, tags=['Клиент'])
def get_workers(customer_id: int, db: Session = Depends(get_db)):
    pass


@app.patch('/customer/{customer_id}/primary_phone', response_model=response_models.BaseResponse, tags=['Клиент'])
def change_customer_primary_phone(customer_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/customer/{customer_id}/phone', response_model=response_models.BaseResponse, tags=['Клиент'])
def add_customer_phone(customer_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/customer/{customer_id}/name', response_model=response_models.BaseResponse, tags=['Клиент'])
def change_customer_name(customer_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
    pass


@app.patch('/customer/{customer_id}/appliances/{appliances_id}', response_model=response_models.BaseResponse,
           tags=['Клиент'])
def add_customer_appliances(appliances_id: int, customer_id: int, new_name: schemas.NewName,
                            db: Session = Depends(get_db)):
    pass


@app.put('/order', response_model=response_models.BaseResponse, tags=['Заказ'])
def create_order(new_order: schemas.CreateOrder, db: Session = Depends(get_db)):
    pass


@app.get('/orders', response_model=response_models.Orders, tags=['Заказ'])
def create_worker(db: Session = Depends(get_db)):
    pass


@app.get('/order/{order_id}', response_model=response_models.Order, tags=['Заказ'])
def get_workers(order_id: int, db: Session = Depends(get_db)):
    pass


@app.patch('/order/{order_id}/worker/{worker_id}', response_model=response_models.BaseResponse, tags=['Заказ'])
def update_worker(order_id: int, worker_id: int, db: Session = Depends(get_db)):
    pass


@app.patch('/order/{order_id}/appliances/{appliances_id}', response_model=response_models.BaseResponse, tags=['Заказ'])
def update_appliances(order_id: int, appliances_id: int, db: Session = Depends(get_db)):
    pass

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import get_db

from . import response_models
from . import schemas

app = FastAPI()


@app.post('/admin/login', response_model=response_models.BaseResponse, tags=['Администратор'])
def admin_login(login_data: schemas.LoginSchema, db: Session = Depends(get_db)):
    pass


@app.put('/admin/', response_model=response_models.BaseResponse, tags=['Администратор'])
def create_admin(new_admin: schemas.CreateAdmin, db: Session = Depends(get_db)):
    pass


@app.get('/admins', response_model=response_models.Admins, tags=['Администратор'])
def get_admins(db: Session = Depends(get_db)):
    pass


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
def change_admin_primary_phone(operator_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/phone', response_model=response_models.BaseResponse, tags=['Оператор'])
def add_admin_phone(operator_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/name', response_model=response_models.BaseResponse, tags=['Оператор'])
def change_admin_name(operator_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
    pass


@app.patch('/operator/{operator_id}/password', response_model=response_models.BaseResponse, tags=['Оператор'])
def change_admin_name(operator_id: int, new_password: schemas.NewPassword, db: Session = Depends(get_db)):
    pass


@app.delete('/operator/{operator_id}/phone', response_model=response_models.BaseResponse, tags=['Оператор'])
def remove_admin_phone(operator_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
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
def add_admin_phone(worker_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/worker/{worker_id}/name', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def change_admin_name(worker_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
    pass


@app.patch('/worker/{worker_id}/password', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def change_admin_name(worker_id: int, new_password: schemas.NewPassword, db: Session = Depends(get_db)):
    pass


@app.delete('/worker/{worker_id}/phone', response_model=response_models.BaseResponse, tags=['Исполнитель'])
def remove_admin_phone(worker_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
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
def change_admin_primary_phone(customer_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/customer/{customer_id}/phone', response_model=response_models.BaseResponse, tags=['Клиент'])
def add_admin_phone(customer_id: int, new_phone: schemas.NewPhone, db: Session = Depends(get_db)):
    pass


@app.patch('/customer/{customer_id}/name', response_model=response_models.BaseResponse, tags=['Клиент'])
def change_admin_name(customer_id: int, new_name: schemas.NewName, db: Session = Depends(get_db)):
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

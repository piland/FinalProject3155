from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import paymentInformation as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['PaymentInformation'],
    prefix="/paymentInformation"
)


@router.post("/", response_model=schema.PaymentInformation)
def create(request: schema.PaymentInformationCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PaymentInformation])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{paymentInformation_id}", response_model=schema.PaymentInformation)
def read_one(paymentInformation_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, paymentInformation_id=paymentInformation_id)


@router.put("/{paymentInformation_id}", response_model=schema.PaymentInformation)
def update(paymentInformation_id: int, request: schema.PaymentInformationUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, paymentInformation_id=paymentInformation_id, request=request)


@router.delete("/{paymentInformation_id}")
def delete(paymentInformation_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, paymentInformation_id=paymentInformation_id)
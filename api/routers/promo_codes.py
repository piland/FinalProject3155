from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promo_codes as controller
from ..schemas import promo_codes as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['PromoCodes'],
    prefix="/promocodes"
)


@router.post("/", response_model=schema.PromoCode)
def create(request: schema.PromoCode, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PromoCode])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{name}", response_model=schema.PromoCode)
def read_one(name: str, db: Session = Depends(get_db)):
    return controller.read_one(db, name=name)


@router.put("/{name}", response_model=schema.PromoCode)
def update(name: str, request: schema.PromoCodeUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, name=name, request=request)


@router.delete("/{name}")
def delete(name: str, db: Session = Depends(get_db)):
    return controller.delete(db=db, name=name)
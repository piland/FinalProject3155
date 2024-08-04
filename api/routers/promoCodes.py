from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promoCodes as controller
from ..schemas import promoCodes as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['PromoCodes'],
    prefix="/promoCodes"
)


@router.post("/", response_model=schema.PromoCode)
def create(request: schema.PromoCode, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PromoCode])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{promo_id}", response_model=schema.PromoCode)
def read_one(promo_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promo_id=promo_id)


@router.put("/{promo_id}", response_model=schema.PromoCode)
def update(promo_id: int, request: schema.PromoCodeUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, promo_id=promo_id, request=request)


@router.delete("/{promo_id}")
def delete(promo_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, promo_id=promo_id)
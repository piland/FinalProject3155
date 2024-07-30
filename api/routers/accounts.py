from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import accounts as controller
from ..schemas import accounts as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Accounts'],
    prefix="/accounts"
)


@router.post("/", response_model=schema.Account)
def create(request: schema.AccountCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Account])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{account_id}", response_model=schema.Account)
def read_one(account_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, account_id=account_id)


@router.put("/{account_id}", response_model=schema.Account)
def update(account_id: int, request: schema.AccountUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, account_id=account_id, request=request)


@router.delete("/{account_id}")
def delete(account_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, account_id=account_id)
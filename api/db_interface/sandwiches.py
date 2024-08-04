from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db, SessionLocal
from api.models.sandwiches import Sandwich

def create_sandwich(sandwich_name: str, price: float):
    with SessionLocal() as db:
        new_sandwich = Sandwich(sandwich_name=sandwich_name, price=price)
        db.add(new_sandwich)
        db.commit()
        db.refresh(new_sandwich)
        return new_sandwich

def get_sandwich_by_id(sandwich_id: int):
    with SessionLocal() as db:
        return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

def get_all_sandwiches():
    with SessionLocal() as db:
        sandwich_list = db.query(Sandwich).all()
        return sandwich_list

def update_sandwich(sandwich_id: int, sandwich_name: str = None, price: float = None):
    with SessionLocal() as db:
        sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
        if sandwich:
            if sandwich_name:
                sandwich.sandwich_name = sandwich_name
            if price:
                sandwich.price = price
            db.commit()
            return sandwich
        return None

def delete_sandwich(sandwich_id: int):
    with SessionLocal() as db:
        sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
        if sandwich:
            db.delete(sandwich)
            db.commit()
            return True
        return False
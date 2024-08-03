from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db
from api.models.resources import Resource

def create_resource(item: str, amount: int, db: Session = get_db()):
    new_resource = Resource(item=item, amount=amount)
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

def get_resource_by_id(resource_id: int, db: Session =  get_db()):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def update_resource(resource_id: int, item: str = None, amount: int = None, db: Session = get_db()):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if resource:
        if item:
            resource.item = item
        if amount:
            resource.amount = amount
        db.commit()
        return resource
    return None

def delete_resource(resource_id: int, db: Session =  get_db()):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if resource:
        db.delete(resource)
        db.commit()
        return True
    return False

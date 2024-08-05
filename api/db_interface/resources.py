from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db, SessionLocal
from api.models.resources import Resource

def create_resource(item: str, amount: int):
    with SessionLocal() as db:
        new_resource = Resource(item=item, amount=amount)
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)
        return new_resource

def get_resource_by_id(resource_id: int):
    with SessionLocal() as db:
        return db.query(Resource).filter(Resource.id == resource_id).first()

def get_all_resources():
    with SessionLocal() as db:
        resource_list = db.query(Resource).all()
        return resource_list

def get_current_resource_dict():
    with SessionLocal() as db:
        resources = db.query(Resource).all()
        resource_dict = {}
        for resource_item in resources:
            resource_dict[f"{resource_item.id}"] = resource_item.amount
        return resource_dict

def update_resource(resource_id: int, item: str = None, amount: int = None):
    with SessionLocal() as db:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if resource:
            if item:
                resource.item = item
            if amount:
                resource.amount = amount
            db.commit()
            db.refresh(resource)
            return resource
        return None

def show_all_resources():
    resource_list = get_all_resources()
    print("\n========== RESOURCE LIST ==========")
    for resource in resource_list:
        print(resource)
    print("===================================")

def delete_resource(resource_id: int):
    with SessionLocal() as db:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if resource:
            db.delete(resource)
            db.commit()
            return True
        return False

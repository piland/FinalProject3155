from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db
from api.models.roles import Role

def create_role(title: str, description: str, db: Session = get_db()):
    new_role = Role(title=title, description=description)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_role_by_id(role_id: str, db: Session =  get_db()):
    return db.query(Role).filter(Role.id == role_id).first()

def update_role(role_id: str, title: str = None, description: str = None, db: Session = get_db()):
    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        if title:
            role.title = title
        if description:
            role.description = description
        db.commit()
        return role
    return None

def delete_role(role_id: str, db: Session =  get_db()):
    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        db.delete(role)
        db.commit()
        return True
    return False
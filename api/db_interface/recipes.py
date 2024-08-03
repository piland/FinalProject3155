from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db
from api.models.recipes import Recipe

def create_recipe(sandwich_id: int, resource_id: int, db: Session = get_db()):
    new_recipe = Recipe(sandwich_id=sandwich_id, resource_id=resource_id)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

def get_recipe_by_id(recipe_id: int, db: Session =  get_db()):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def update_recipe(recipe_id: int, sandwich_id: int = None, resource_id: int = None, db: Session = get_db()):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if recipe:
        if sandwich_id:
            recipe.sandwich_id = sandwich_id
        if resource_id:
            recipe.resource_id = resource_id
        db.commit()
        return recipe
    return None

def delete_recipe(recipe_id: int, db: Session =  get_db()):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if recipe:
        db.delete(recipe)
        db.commit()
        return True
    return False
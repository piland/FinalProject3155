from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db, SessionLocal
from api.models.recipes import Recipe

def create_recipe(sandwich_id: int, resource_id: int):
    with SessionLocal() as db:
        new_recipe = Recipe(sandwich_id=sandwich_id, resource_id=resource_id)
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
        return new_recipe

def get_recipe_by_id(recipe_id: int):
    with SessionLocal() as db:
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def update_recipe(recipe_id: int, sandwich_id: int = None, resource_id: int = None, amount: float = None):
    with SessionLocal() as db:
        recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if recipe:
            if sandwich_id:
                recipe.sandwich_id = sandwich_id
            if resource_id:
                recipe.resource_id = resource_id
            if amount:
                recipe.amount = amount
            db.commit()
            return recipe
        return None

def get_recipe_dict(sandwich_id):
    with SessionLocal() as db:
        recipe = db.query(Recipe).filter(Recipe.sandwich_id == sandwich_id).all()
        recipe_dict = {}
        for recipe_item in recipe:
            recipe_dict[f"{recipe_item.resource_id}"] = recipe_item.amount
        return recipe_dict

def delete_recipe(recipe_id: int):
    with SessionLocal() as db:
        recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if recipe:
            db.delete(recipe)
            db.commit()
            return True
        return False

print(get_recipe_dict(1))
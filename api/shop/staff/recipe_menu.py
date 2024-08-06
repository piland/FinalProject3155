from api.db_interface import recipes, resources, sandwiches
from api.models.sandwiches import Sandwich
from api.models.recipes import Recipe
from api.models.resources import Resource
from api.dependencies.database import SessionLocal
def recipe_menu():
    exit = 0
    valid_option_selected = 0
    while exit != 1:
        while valid_option_selected != 1:
            option = -1
            print("\n======= RECIPE EDITOR ========")
            print("1. Modify Sandwich Recipe")
            print("0. Exit to Main Menu")

            try:
                option = int(input("\nEnter One of the Options Above: "))
                if option > -1 and option < 7:
                    valid_option_selected = 1
            except:
                print("Invalid Option")

        if option == 0:
            exit = 1
        elif option == 1:
            modify_sandwich_recipe()
        valid_option_selected = 0

def modify_sandwich_recipe():
    with SessionLocal() as db:
        sandwiches.show_all_sandwiches()
        sandwich_id_accepted = 0
        while sandwich_id_accepted == 0:
            sandwich_id = input("Enter Sandwich ID: ")
            try:
                sandwich_id = int(sandwich_id)
                sandwich = db.query(Sandwich).filter(sandwich_id == Sandwich.id).first()
                sandwich_id_accepted = 1
            except:
                print("ERROR: ID must be Integer and Exist in Sandwiches")
        editing_recipe = 1
        while editing_recipe == 1:
            show_recipe_for_sandwich(sandwich)
            resource_id_accepted = 0
            while resource_id_accepted == 0:
                resource_id = input("Enter ID of Resource to be Edited (Exit/e to End Editing): ")
                if resource_id.lower() == "exit" or resource_id.lower() == "e":
                    editing_recipe = 0
                    break
                else:
                    try:
                        resource_id = int(resource_id)
                        selected_recipe_item = db.query(Recipe).filter((resource_id == Recipe.resource_id) & (Recipe.sandwich_id == sandwich.id)).first()
                        resource_id_accepted = 1
                    except:
                        print("ERROR: ID must be Integer and Exist in Recipe")
            if editing_recipe == 0:
                break
            new_quantity_accepted = 0
            while new_quantity_accepted == 0:
                resource_name = db.query(Resource).filter(resource_id == Resource.id).first().item
                new_quantity = input(f"Enter New Amount of {resource_name} for {sandwich.sandwich_name}: ")
                try:
                    new_quantity = int(new_quantity)
                    recipes.update_recipe(selected_recipe_item.id, amount = new_quantity)
                    new_quantity_accepted = 1
                except:
                    print("ERROR: Quantity must be Number")
        show_recipe_for_sandwich(sandwich)

def show_recipe_for_sandwich(sandwich):
    with SessionLocal() as db:
        print(f"\n===== {sandwich.sandwich_name} RECIPE =====")
        for recipe_item in sandwich.recipes:
            resource_name = db.query(Resource).filter(recipe_item.resource_id == Resource.id).first().item
            print(f"{recipe_item.resource_id}. {resource_name}: {recipe_item.amount}")
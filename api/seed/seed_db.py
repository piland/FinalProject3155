# api/utils/seeder.py
from sqlalchemy.orm import Session
from api.models.roles import Role
from api.models.promo_codes import PromoCode
from api.models.sandwiches import Sandwich
from api.models.resources import Resource
from api.dependencies.database import SessionLocal, engine, Base
from api.models.payment_information import PaymentInformation


def seed_db():
    # Create the database and tables if they don't exist
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    try:
        #Check if data already exists
        if db.query(Role).count() == 0:
            roles = [
                Role(id=1, title="Guest", description="Guest with no privileges or account management abilities"),
                Role(id=2, title="Member", description="Regular member with account management abilities"),
                Role(id=3, title="Staff", description="Staff with menu editing, inventory management privilege"),
                Role(id=4, title="Chef", description="Chef with limited privilege, but can manage inventory"),
                Role(id=5, title="Manager", description="Manager with full privilege")
            ]
            db.add_all(roles)
            db.commit()
        if db.query(PromoCode).count() == 0:
            promo_codes = [
                PromoCode(id=1, name="GRANDOPENING", discount=0.80),
                PromoCode(id=2, name="ILOVEHAMSANDWICHES", discount=0.01)
            ]
            db.add_all(promo_codes)
            db.commit()
        if db.query(Sandwich).count() == 0:
            sandwiches = [
                Sandwich(id=1, sandwich_name="Small Ham Sandwich", price=5.00),
                Sandwich(id=2, sandwich_name="Regular Ham Sandwich", price=6.50),
                Sandwich(id=3, sandwich_name="Large Ham Sandwich", price=8.00),
                Sandwich(id=4, sandwich_name="Small Double Ham Sandwich", price=7.00),
                Sandwich(id=5, sandwich_name="Regular Double Ham Sandwich", price=8.50),
                Sandwich(id=6, sandwich_name="Large Double Ham Sandwich", price=10.00)
            ]
            db.add_all(sandwiches)
            db.commit()
        if db.query(Resource).count() == 0:
            resources = [
                Resource(id=1, item="Bread", amount=50, price=0.25),
                Resource(id=2, item="Ham", amount=50, price=0.75),
                Resource(id=3, item="Cheese", amount=50, price=0.25),
                Resource(id=4, item="Tomato", amount=50, price=0.50),
                Resource(id=5, item="Pickles", amount=50, price=0.15),
                Resource(id=6, item="Lettuce", amount=50, price=0.25),
                Resource(id=7, item="Mayo", amount=50, price=0.75),
                Resource(id=8, item="Onions", amount=50, price=0.25)
            ]
            db.add_all(resources)
            db.commit()
        if db.query(PaymentInformation).count() == 0:
            payments = [
                PaymentInformation(id=1, balance_on_account=0, card_information="None", payment_type="None",
                                   last_transaction_status=False)
            ]
            db.add_all(payments)
            db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error seeding: {e}")
    finally:
        db.close()

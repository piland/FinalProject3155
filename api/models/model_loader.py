from . import orders, order_details, recipes, sandwiches, resources, accounts, roles, paymentInformation, reviews, promoCodes
from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    accounts.Base.metadata.create_all(engine)
    roles.Base.metadata.create_all(engine)
    paymentInformation.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)

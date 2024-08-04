from . import orders, order_details, accounts, payment_information, reviews, roles, promo_codes


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(accounts.router)
    app.include_router(payment_information.router)
    app.include_router(reviews.router)
    app.include_router(roles.router)
    app.include_router(promo_codes.router)

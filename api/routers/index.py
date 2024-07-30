from . import orders, order_details, accounts, paymentInformation, reviews


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(accounts.router)
    app.include_router(paymentInformation.router)
    app.include_router(reviews.router)

from sqlalchemy.orm import Session
import api.models
import api.schemas
from api.models import roles as roles_model


def dbseed(db: Session):
    # Seed for Roles
    manager = roles_model.Role(
        id=1,
        title="Manager",
        description="Manager Role; can edit order history, incharge of inventory, and manage the kitchen line."
    )
    staff = roles_model.Role(
        id=2,
        title="Staff",
        description="Staff Role; in charge of prep, inventory, helping the cooks, can help with the inventory."
    )
    cook = roles_model.Role(
        id=3,
        title="Cook",
        description="Cook Role; in charge of cooking quality food, and ensuring a safe environment in the kitchen."
    )
    member = roles_model.Role(
        id=4,
        title="Member",
        description="Member Role; a member who can save payment information and their address for future purchases, "
                    "and leave reviews."
    )
    guest = roles_model.Role(
        id=5,
        title="Guest",
        description="Guest Role; someone who orders without making an account"
    )
    db.add(manager)
    db.add(staff)
    db.add(cook)
    db.add(member)
    db.add(guest)
    db.commit()


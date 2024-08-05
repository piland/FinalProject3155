import api.models.accounts
import api.controllers.accounts
import api.schemas.accounts
import api.routers.accounts
import api.requests.accounts
import api.controllers.roles
import api.requests.payment_information
from api.dependencies.database import SessionLocal


class AccountManagement:
    def __init__(self):
        pass

    """========== LOGIN OR SIGNUP ============"""
    """=================================="""

    def login_menu(self):
        print("\n======= Welcome ========")
        while True:
            print("1. Login")
            print("2. Signup")
            print("3. Continue as Guest")
            print("4. Update Payment Information")
            print("5. Exit")
            option = input("Please enter the number you would like to do: ")

            if option.isdigit() and int(option) in range(1, 5):
                option = int(option)
                match option:
                    case 1:
                        account_id = self.login()
                        return account_id
                    case 2:
                        account_id = self.register_account()
                        return account_id
                    case 3:
                        return self.guest_login()
                    case 4:
                        account_id = self.handle_update_payment_information()
                        return account_id
                    case 5:
                        exit()
            else:
                print("Invalid option. Please try again.")

    def login(self):
        email = input("Please enter your email address: ")
        password = input("Please enter your password: ")

        # Fetch user id
        response = api.requests.accounts.read_by_email(email)
        # Check if password is correct
        if response:
            account_id = response.get("id")
            if response.get("password") == password:
                print(f"Welcome back, {response['name']}")
                return account_id
            else:
                print("Invalid password. Please try again.")
        else:
            print("No account found with this email. Please try again.")
        return None

    def handle_update_payment_information(self):
        print("Please log in before updating payment information")
        account_id = self.login()
        if account_id:
            print("Thank you, please update your payment information")
            payment_information = self.get_payment_information(account_id)
            if payment_information:
                payment_information_id = payment_information.get("id")
                balance = input("What is your new balance? ")
                card_info = input("What is your new card number? ")
                payment_type = input("What is your new payment type? ")
                self.update_payment_information(payment_information_id, balance, card_info, payment_type)
        return account_id

    def get_payment_information(self, account_id):
        response = api.requests.accounts.read_one(account_id)
        if response:
            payment_information_id = response.get("payment_information_id")
            if payment_information_id:
                return api.requests.payment_information.read_one(payment_information_id)
        print("No payment information found for this account.")
        return None

    def update_payment_information(self, payment_information_id, balance, card_info, payment_type):
        response = api.requests.payment_information.update(
            payment_information_id=payment_information_id,
            balance_on_account=balance,
            card_information=card_info,
            payment_type=payment_type
        )
        if response:
            print(f"Payment Information Updated Successfully: {response}")
            return response
        else:
            print("Failed to Update Payment Information")
            return None

    def register_account(self):
        name = input("What is your name? ")
        age = input("What is your age? ")
        phone = input("What is your phone number? ")
        email = input("What is your email address? ")
        password = input("What do you want your password to be?\nMust be five or more characters: ")
        while len(password) < 5:
            print("Password must be at least five characters.")
            password = input("What do you want your password to be?\nMust be five or more characters: ")

        print("What is your role?")
        roles = api.controllers.roles.read_all(db=SessionLocal())
        for role in roles:
            print(f"{role['id']}: {role['name']}, {role['description']}")
        role_id = input("Role ID: ")
        while not role_id.isdigit() or int(role_id) not in [role['id'] for role in roles]:
            print("Sorry, that isn't a valid role. Please choose one of the above numbers.")
            role_id = input("Role ID: ")
        role_id = int(role_id)

        answer = input("Would you like to store your payment information? (Y/N): ").lower()
        while answer not in ["y", "n"]:
            print("Please enter either 'y' or 'n'.")
            answer = input("Would you like to store your payment information? (Y/N): ").lower()

        payment_information_id = None
        if answer == "y":
            balance = input("What is your balance? ")
            card_info = input("What is your card number? ")
            payment_type = input("What is your payment type? ")
            payment_info = self.create_payment_information(balance, card_info, payment_type)
            if payment_info:
                payment_information_id = payment_info['id']

        response = api.requests.accounts.create(
            name=name,
            age=int(age) if age else None,
            phone_number=phone,
            email=email,
            password=password,
            role_id=role_id,
            payment_information_id=payment_information_id
        )

        if response:
            account_id = response.get("id")
            print(f"Account Created Successfully: {response}")
            return account_id
        else:
            print("Failed to Create Account")
        return None

    def guest_login(self):
        print("Continuing as Guest.")
        return api.requests.accounts.read_one(1)

    def create_payment_information(self, balance, card_info, payment_type):
        response = api.requests.payment_information.create(
            balance_on_account=balance,
            card_information=card_info,
            payment_type=payment_type
        )
        if response:
            print(f"Payment Information Created Successfully: {response}")
            return response
        else:
            print("Failed to Create Payment Information")
            return None

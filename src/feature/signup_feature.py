from navigation import navigation_service
from user import user_service
from security import security_service
from getpass import getpass
from user import user_service, User
from feature import home_feature


def go_to_signup():
    """
    Function to handle the signup feature.

    This function prompts the user to enter their email, password, first name, and last name.
    It then checks if the email already exists in the user database.
    If the email exists, it displays an error message and redirects the user to the home feature.
    If the email doesn't exist, it hashes the password, creates a new user object, and adds it to the user database.
    Finally, it displays a success message and redirects the user to the home feature.
    """
    navigation_service.navigate("Signup")

    user = {"id": None, "role": "borrower"}

    user["email"] = input("Email: ")

    if user_service.find_one_with_email(user["email"]):
        navigation_service.focus_message("Email already exists.")
        home_feature.go_to_home()
    else:
        user["password"] = security_service.hash_string(getpass("Password: "))
        user["first_name"] = input("First Name: ")
        user["last_name"] = input("Last Name: ")

        user_service.create(User(**user))

        navigation_service.focus_message("Sign up successful.")
        home_feature.go_to_home()


signup_option = {"title": "Signup", "callback": go_to_signup}

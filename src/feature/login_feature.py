from navigation import navigation_service
from security import security_service
from feature import home_feature
from user import user_service
from getpass import getpass
from feature.admin import admin_dashboard
from feature.borrower import borrower_dashboard
from feature.borrower import borrower_operation


def go_to_login():
    """
    Function to handle the login feature of the library management system.

    This function prompts the user to enter their email and password,
    verifies the credentials, and navigates to the appropriate dashboard
    based on the user's role (admin or borrower).

    Args:
        None

    Returns:
        None
    """
    navigation_service.navigate("Login")

    email = input("Email: ")
    password = getpass("Password: ")

    user = user_service.find_one_with_email(email)

    if not user or user.password != security_service.hash_string(password):
        navigation_service.focus_message("Email or password is incorrect.")
        home_feature.go_to_home()
    else:
        if user.role == "borrower":
            # go to borrower page
            borrower_operation.user_details(user)
            borrower_dashboard.go_to_borrower()

        elif user.role == "admin":
            # go to admin page
            admin_dashboard.admin_dashboard()


login_option = {"title": "Login", "callback": go_to_login}

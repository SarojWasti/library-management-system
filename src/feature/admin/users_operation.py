from user import user_service
from feature.admin import admin_dashboard


def display_user():
    """
    Displays all the users in the system.
    """
    get_users()
    admin_dashboard.proxy()


def delete_user():
    """
    Deletes a user from the system.
    """
    get_users()
    user_id = int(input("Please enter the user id to delete: "))
    user_service.delete(user_id=user_id)
    print("User has been deleted successfully!")
    admin_dashboard.proxy()


def get_users():
    """
    Retrieves all the users from the database and prints their details.
    """
    all_users = user_service.find_all()
    if all_users.count != 0:
        head = f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'User Role'}"
        print(head)
        print("-" * (len(head)))
        for user in all_users:
            print(f"{user.id:<5}{user.first_name:<15}{user.last_name:<15}{user.role}")
    else:
        print("No users found!")


display_user_option = {"title": "Display All Users", "callback": display_user}
delete_user_option = {"title": "Delete a User", "callback": delete_user}

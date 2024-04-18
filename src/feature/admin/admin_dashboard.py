from feature.admin import book_operations
from navigation import navigation_service
from feature.admin import users_operation


def admin_dashboard():
    """
    Function to display the admin dashboard and navigate to different options.
    """
    navigation_service.navigate(
        "Admin Panel",
        {
            "a": book_operations.add_books_option,
            "b": book_operations.display_books_option,
            "c": book_operations.books_borrowed_option,
            "d": book_operations.delete_books_option,
            "e": users_operation.display_user_option,
            "f": users_operation.delete_user_option,
        },
    )


def proxy():
    """
    Function to prompt the user to continue and then call the admin_dashboard function.
    """
    input("\nPlease enter to continue...")
    admin_dashboard()

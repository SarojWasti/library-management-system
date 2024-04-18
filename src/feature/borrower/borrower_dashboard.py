from navigation import navigation_service
from feature.borrower import borrower_operation


def go_to_borrower():
    """
    Navigates to the borrower dashboard.

    This function uses the `navigation_service` module to navigate to the borrower dashboard.
    It provides options for viewing, borrowing, searching, and returning books.

    Args:
        None

    Returns:
        None
    """
    navigation_service.navigate(
        "Borrower",
        {
            "a": borrower_operation.view_book_option,
            "b": borrower_operation.borrow_book_option,
            "c": borrower_operation.search_book_option,
            "d": borrower_operation.return_book_option,
        },
    )


def proxy():
    """
    Proxy function for pausing execution.

    This function prompts the user to press Enter to continue.
    After the user presses Enter, it calls the `go_to_borrower` function.

    Args:
        None

    Returns:
        None
    """
    input("Please Enter to continue...")
    go_to_borrower()

from feature import display_books
from feature.borrower import borrower_dashboard
from book import book_service
from borrow import borrow_service

details = []


def user_details(user):
    """
    Store the user details in the 'details' list.

    Args:
    - user: The user object containing the user details.
    """
    details.insert(0, user.id)


def return_book():
    """
    Return a borrowed book.

    This function displays the books borrowed by the user and prompts the user to enter the Borrow ID of the book they want to return.
    If the Borrow ID is valid, the book is returned and removed from the borrow_service.
    """
    user_id = details[0]
    book_borrowed = borrow_service.find_all()

    if book_borrowed and user_id in [borrow.user_id for borrow in book_borrowed]:
        print(f"Books You have borrowed {'-'*50}\n")
        print(f"{'Borrow ID':<12}{'Book ID':<10}{'Book Name':<30}{'Author'}")

        for borrow in book_borrowed:
            if user_id == borrow.user_id:
                book_details = book_service.find_one(book_id=borrow.book_id)
                print(
                    f"{borrow.id:<12}{book_details.id:<10}{book_details.title:<30}{book_details.author}"
                )

        borrow_id = int(input("Please enter a Borrow ID to return the book: "))

        borrow_service.delete(borrow_id=borrow_id)

        print("Book has been successfully returned!\n")

    else:
        print("You haven't borrowed any books!")

    borrower_dashboard.proxy()


def view_book():
    """
    View all available books.

    This function retrieves all the books from the book_service and displays them using the display_books module.
    The user is then prompted to either borrow a book or return to the borrower dashboard.
    """
    books = book_service.find_all()
    display_books.display_all_books(books=books)
    if input("Would you like to borrow a book? Y/N: ").lower() == "y":
        borrow_proxy()
    borrower_dashboard.proxy()


def borrow_book():
    """
    Borrow a book.

    This function retrieves all the available books from the book_service and displays them using the display_books module.
    The user is then prompted to enter the book ID of the book they want to borrow.
    If the book ID is valid and the user has not already borrowed the book, the book is borrowed and added to the borrow_service.
    """
    books = book_service.find_all()
    display_books.display_all_books(books=books)
    borrow_proxy()
    borrower_dashboard.proxy()


def borrow_proxy():
    """
    Proxy function for borrowing a book.

    This function is called by both the borrow_book and search_book functions.
    It prompts the user to enter the book ID of the book they want to borrow.
    If the book ID is valid and the user has not already borrowed the book, the book is borrowed and added to the borrow_service.
    """
    book_id = int(input("Please enter a book id to borrow: "))
    existing_instance = borrow_service.find_all()
    match = False
    for exist in existing_instance:
        if details[0] == exist.user_id and book_id == exist.book_id:
            print("You have already borrowed that book!")
            match = True
    if not match:
        borrow_instance = borrow_service.Borrow(
            id=None, user_id=details[0], book_id=book_id
        )
        borrow_service.create(borrow_instance)
        print("You've successfully borrowed the book!")


def search_book():
    """
    Search for a book.

    This function prompts the user to enter a search query (book title, author name, or genre).
    It then searches for books in the book_service that match the query and displays the results using the display_books module.
    If any matching books are found, the user is prompted to borrow a book.
    """
    query = input("Enter book title or author name or genre: ").strip().lower()
    books = book_service.find_all()
    found_books = []
    for book in books:
        if (
            query in book.title.lower()
            or query in book.author.lower()
            or query in book.genre.lower()
        ):
            found_books.append(book)

    if found_books:
        print(f"Found {len(found_books)} books matching your search:")
        display_books.display_all_books(found_books)
        if input("Would you like to borrow a book? (Y/N) ").lower() == "y":
            borrow_proxy()
    else:
        print("No books found matching your search.")

    borrower_dashboard.proxy()


borrow_book_option = {"title": "Borrow Book", "callback": borrow_book}

search_book_option = {"title": "Search for book", "callback": search_book}

view_book_option = {"title": "View All Books", "callback": view_book}

return_book_option = {"title": "Return Books", "callback": return_book}

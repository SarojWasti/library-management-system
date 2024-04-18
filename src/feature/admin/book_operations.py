from book import book_service
from database import DB_NAME
from feature.admin import admin_dashboard
from feature import display_books
from borrow import borrow_service
from user import user_service


def add_books():
    """
    Adds a new book to the library.

    Prompts the user to enter the book details such as title, author, ISBN, genre, publication year,
    publisher, and number of pages. Creates a new Book object with the entered details and calls the
    book_service.create() method to add the book to the library. Finally, displays a success message.

    Args:
        None

    Returns:
        None
    """
    print("Please enter book details!")
    title = input("Book Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    genre = input("Genre: ")
    publication_year = int(input("Publication Year: "))
    publisher = input("Publisher: ")
    number_of_pages = int(input("Number of pages: "))
    add_book = book_service.Book(
        id=None,
        title=title,
        author=author,
        isbn=isbn,
        genre=genre,
        publication_year=publication_year,
        publisher=publisher,
        number_of_pages=number_of_pages,
    )

    book_service.create(add_book)
    print("Book has been added!\n")

    admin_dashboard.proxy()


def display_book():
    """
    Displays all the books in the library.

    Calls the book_service.find_all() method to retrieve all the books from the library. Then, calls
    the display_books.display_all_books() method to display the books. Finally, calls the admin_dashboard.proxy()
    method to return to the admin dashboard.

    Args:
        None

    Returns:
        None
    """
    books = book_service.find_all()
    display_books.display_all_books(books=books)
    admin_dashboard.proxy()


def display_borrowed():
    """
    Displays all the borrowed books.

    Calls the borrow_service.find_all() method to retrieve all the borrowed books. If there are borrowed books,
    it prints the details of each borrowed book including the borrow ID, user name, and book name. If there are
    no borrowed books, it prints a message indicating that no books have been borrowed yet. Finally, it calls the
    admin_dashboard.proxy() method to return to the admin dashboard.

    Args:
        None

    Returns:
        None
    """
    book_borrowed = borrow_service.find_all()
    if book_borrowed:
        print(f"Borrowed Books:{'-'*50}\n")
        print(f"{'Borrow ID':<12}{'User Name':<20}{'Book Name'}")
        for borrow in book_borrowed:
            user_details = user_service.find_one(user_id=borrow.user_id)
            book_details = book_service.find_one(book_id=borrow.book_id)
            print(
                f"{borrow.id:<12}{user_details.first_name} {user_details.last_name:<14}{book_details.title}"
            )
    else:
        print("No books have been borrowed yet!")
    admin_dashboard.proxy()


def delete_books():
    """
    Deletes a book from the library.

    Calls the book_service.find_all() method to retrieve all the books from the library. Then, calls
    the display_books.display_all_books() method to display the books. Prompts the user to enter the
    ID of the book to be deleted. Calls the book_service.delete() method to delete the book. Finally,
    displays a success message.

    Args:
        None

    Returns:
        None
    """
    display = book_service.find_all()
    display_books.display_all_books(display)
    book_id = int(input("\nEnter book id to remove the book: "))
    book_service.delete(book_id=book_id)
    print("Book deleted successfully!\n")
    admin_dashboard.proxy()


add_books_option = {"title": "Add Books", "callback": add_books}

display_books_option = {"title": "Display Books", "callback": display_book}

delete_books_option = {"title": "Delete Book", "callback": delete_books}

books_borrowed_option = {"title": "View Borrowed Books", "callback": display_borrowed}

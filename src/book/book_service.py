from sqlite3 import connect, Row
from database import DB_NAME
from book import Book


def create(book_instance) -> None:
    """
    Creates a new book record in the database.

    Args:
        book_instance (Book): The book instance to be created.

    Returns:
        None
    """
    with connect(DB_NAME) as connection:
        delattr(book_instance, "id")

        connection.cursor().execute(
            """insert into books (
                title,
                author,
                isbn,
                genre,
                publication_year,
                publisher,
                number_of_pages) values (?, ?, ?, ?, ?, ?, ?)
            """,
            tuple(book_instance.__dict__.values()),
        )


def find_all() -> list[Book]:
    """
    Retrieves all books from the database.

    Returns:
        list[Book]: A list of Book instances representing all the books in the database.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        return [
            Book(**book)
            for book in connection.cursor().execute("select * from books").fetchall()
        ]


def find_one(book_id) -> Book:
    """
    Retrieves a specific book from the database based on its ID.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        Book: The Book instance representing the retrieved book.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        return Book(
            **connection.cursor()
            .execute("select * from books where id = ?", (book_id,))
            .fetchone()
        )


def delete(book_id) -> None:
    """
    Deletes a book record from the database based on its ID.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        None
    """
    with connect(DB_NAME) as connection:
        return connection.cursor().execute("delete from books where id = ?", (book_id,))

class Book:
    """
    Represents a book in the library management system.

    Attributes:
        id (int): The unique identifier of the book.
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN (International Standard Book Number) of the book.
        genre (str): The genre of the book.
        publication_year (int): The year of publication of the book.
        publisher (str): The publisher of the book.
        number_of_pages (int): The number of pages in the book.
    """

    def __init__(
        self,
        id,
        title,
        author,
        isbn,
        genre,
        publication_year,
        publisher,
        number_of_pages,
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_year = publication_year
        self.publisher = publisher
        self.number_of_pages = number_of_pages

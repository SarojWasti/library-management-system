class Borrow:
    """
    Represents a borrowing record in the library management system.

    Attributes:
        id (int): The unique identifier for the borrowing record.
        user_id (int): The ID of the user who borrowed the book.
        book_id (int): The ID of the book that was borrowed.
    """

    def __init__(self, id, user_id, book_id) -> None:
        self.id = id
        self.user_id = user_id
        self.book_id = book_id

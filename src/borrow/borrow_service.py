from sqlite3 import connect, Row
from database import DB_NAME
from borrow import Borrow


def create(borrow_instance) -> None:
    """
    Creates a new borrow record in the database.

    Args:
        borrow_instance (Borrow): The Borrow instance to be created.

    Returns:
        None
    """
    with connect(DB_NAME) as connection:
        delattr(borrow_instance, "id")

        connection.cursor().execute(
            """insert into borrows (
                user_id,
                book_id) values (?, ?)
            """,
            tuple(borrow_instance.__dict__.values()),
        )


def find_all() -> list[Borrow]:
    """
    Retrieves all borrow records from the database.

    Returns:
        list[Borrow]: A list of Borrow instances representing all the borrow records.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        return [
            Borrow(**borrow)
            for borrow in connection.cursor()
            .execute("select * from borrows")
            .fetchall()
        ]


def find_one(borrow_id) -> Borrow:
    """
    Retrieves a specific borrow record from the database.

    Args:
        borrow_id (int): The ID of the borrow record to retrieve.

    Returns:
        Borrow: The Borrow instance representing the retrieved borrow record.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        return Borrow(
            **connection.cursor()
            .execute("select * from borrows where id = ?", (borrow_id,))
            .fetchone()
        )


def delete(borrow_id) -> None:
    """
    Deletes a borrow record from the database.

    Args:
        borrow_id (int): The ID of the borrow record to delete.

    Returns:
        None
    """
    with connect(DB_NAME) as connection:
        return connection.cursor().execute(
            "delete from borrows where id = ?", (borrow_id,)
        )

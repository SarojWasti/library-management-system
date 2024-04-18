from sqlite3 import connect, Row
from database import DB_NAME
from user import User


def create(user_instance) -> None:
    """
    Create a new user in the database.

    Args:
        user_instance (User): The user instance to be created.

    Returns:
        None
    """
    with connect(DB_NAME) as connection:
        delattr(user_instance, "id")

        connection.cursor().execute(
            """insert into users (
                role,
                email,
                password,
                first_name,
                last_name) values (?, ?, ?, ?, ?)
            """,
            tuple(user_instance.__dict__.values()),
        )


def find_all() -> list[User]:
    """
    Retrieve all users from the database.

    Returns:
        list[User]: A list of User instances representing all the users in the database.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        return [
            User(**user)
            for user in connection.cursor().execute("select * from users").fetchall()
        ]


def find_one(user_id) -> User:
    """
    Retrieve a user from the database by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The User instance representing the retrieved user, or None if not found.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        return User(
            **connection.cursor()
            .execute("select * from users where id = ?", (user_id,))
            .fetchone()
        )


def delete(user_id) -> None:
    """
    Delete a user from the database by their ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        None
    """
    with connect(DB_NAME) as connection:
        return connection.cursor().execute("delete from users where id = ?", (user_id,))


def find_one_with_email(email) -> User:
    """
    Retrieve a user from the database by their email.

    Args:
        email (str): The email of the user to retrieve.

    Returns:
        User: The User instance representing the retrieved user, or None if not found.
    """
    with connect(DB_NAME) as connection:
        connection.row_factory = Row

        user = (
            connection.cursor()
            .execute("select * from users where email = ?", (email,))
            .fetchone()
        )

        return User(**user) if user else None

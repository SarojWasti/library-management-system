"""
This module initializes the database for the library management system.

It creates tables for books, users, and borrows if they don't already exist.
It also inserts a super admin user into the users table if it doesn't already exist.
"""

from sqlite3 import connect
from user import User
from security import security_service

DB_NAME = "library.sqlite"

super_admin = User(
    **{
        "id": None,
        "role": "admin",
        "email": "super.admin@library.ca",
        "password": security_service.hash_string("admin"),
        "first_name": "Super",
        "last_name": "Admin",
    }
)
delattr(super_admin, "id")

with connect(DB_NAME) as connection:
    cursor = connection.cursor()

    cursor.execute(
        """create table if not exists books (
            id integer primary key autoincrement,
            title text not null,
            author text not null,
            isbn text not null,
            genre text not null,
            publication_year integer not null,
            publisher text not null,
            number_of_pages integer not null
        )"""
    )

    cursor.execute(
        """create table if not exists users (
            id integer primary key autoincrement,
            role text not null,
            email text not null,
            password text not null,
            first_name text not null,
            last_name text not null,
            constraint unique_email unique (email)
        )"""
    )

    cursor.execute(
        """create table if not exists borrows (
            id integer primary key autoincrement,
            user_id integer not null,
            book_id integer not null
        )"""
    )

    if not cursor.execute(
        "select * from users where email = ?", (super_admin.email,)
    ).fetchone():
        cursor.execute(
            """insert into users (
                role,
                email,
                password,
                first_name,
                last_name) values (?, ?, ?, ?, ?)
            """,
            tuple(super_admin.__dict__.values()),
        )

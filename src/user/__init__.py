class User:
    """
    Represents a user in the library management system.

    Attributes:
        id (int): The unique identifier of the user.
        role (str): The role of the user (e.g., 'admin', 'student', 'librarian').
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, id, role, email, password, first_name, last_name) -> None:
        self.id = id
        self.role = role
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

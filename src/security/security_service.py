from hashlib import md5


def hash_string(string):
    """
    Hashes the given string using MD5 algorithm and a predefined salt.

    Args:
        string (str): The string to be hashed.

    Returns:
        str: The hashed string.

    """
    SALT = "o153XL0uEhJdEzJXnDIJOayMzsbSqp0cHylm4iYP2Rs="

    return md5(f"{string}{SALT}".encode()).hexdigest()

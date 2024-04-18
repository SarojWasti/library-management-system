def display_all_books(books):
    """
    Display all the books in a formatted table.

    Args:
        books (list): A list of book objects.

    Returns:
        None
    """
    if books:
        head = f"{'ID':<5}{'Title':<30}{'Author':<18}{'ISBN':<16}{'Genre':<15}{'Year':<8}{'Publisher':<15}{'Pages'}"
        print(head)
        print("-" * len(head))
        for book in books:
            print(
                f"{book.id:<5}{book.title:<30}{book.author:<18}{book.isbn:<16}{book.genre:<15}{book.publication_year:<8}{book.publisher:<15}{book.number_of_pages}"
            )
    else:
        print("No books found")
    print("\n")

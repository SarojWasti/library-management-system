from os import system, name


def clear_terminal():
    system("cls" if name == "nt" else "clear")


def focus_message(message):
    clear_terminal()
    print(f"{message}\n")
    input("Enter to continue...")


def navigate(title, options={}):
    """
    Navigate through a menu with the given title and options.

    Parameters:
    - title (str): The title of the menu.
    - options (dict): A dictionary containing menu options as keys and their corresponding details as values.
                    Each option's details should include a "title" for display and a "callback" function.

    Returns:
    None

    Usage:
    - Call navigate with the desired title and options to display a menu.
    - The user can choose an option by entering the corresponding key.
    - The menu will continue to be displayed until the user enters 'x' to exit.

    Example:
    navigate("Main Menu", {"1": {"title": "Option 1", "callback": option1_func},
                        "2": {"title": "Option 2", "callback": option2_func},
                        "x": {"title": "Exit"}})
    """
    option = None

    while option not in list(options.keys()) + ["x"]:
        clear_terminal()
        print(f"{title} · Library\n\n")

        if len(options) == 0:
            return

        for k, v in (options | {"x": {"title": "Exit"}}).items():
            print(f"{k}: {v['title']}")

        option = input("\nEnter option: ")

    if option != "x":
        options[option]["callback"]()

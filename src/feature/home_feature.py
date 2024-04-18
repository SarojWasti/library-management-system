from navigation import navigation_service
from feature.login_feature import login_option
from feature.signup_feature import signup_option


def go_to_home():
    """
    Navigates to the home feature.

    This function uses the `navigation_service` module to navigate to the home feature.
    It provides two options: login and signup.

    Args:
        None

    Returns:
        None
    """
    navigation_service.navigate("Home", {"a": login_option, "b": signup_option})

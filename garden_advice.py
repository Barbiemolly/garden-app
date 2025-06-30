# TODO: Create a function for getting gardening tips based on month
# TODO: Replace hardcoded values with a data dictionary
# TODO: Add docstrings for all functions

def get_gardening_tip(month):
    """
    Return gardening advice based on the provided month.

    Args:
        month (str): The name of the month (e.g., "June", "December").

    Returns:
        str: A relevant gardening tip for the month, or a default message if not found.
    """
    tips = {
        "January": "Plan your spring garden and order seeds.",
        "February": "Start seedlings indoors for early crops.",
        "March": "Prepare garden beds and prune shrubs.",
        "April": "Plant cool-season vegetables.",
        "May": "Start planting warm-season crops.",
        "June": "Protect your plants from frost.",
        "July": "Mulch to retain soil moisture.",
        "August": "Harvest summer crops and plant fall vegetables.",
        "September": "Begin fall clean-up and plant perennials.",
        "October": "Protect tender plants from frost.",
        "November": "Compost fallen leaves.",
        "December": "Water your plants early in the morning.",
    }

    return tips.get(month, "Check your local gardening calendar.")


if __name__ == "__main__":
    # Example usage: print gardening tip for a specified month
    current_month = "June"
    print(get_gardening_tip(current_month))

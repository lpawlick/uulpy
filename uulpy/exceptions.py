# exceptions.py

class DuplicateCurrencyName(ValueError):
    """
    Exception raised when attempting to add a currency to the uul object that already exists.

    :param name: The name of the currency causing the duplication.
    :type name: str
    """

    def __init__(self, name: str):
        super().__init__(f"Duplicate currency name: '{name}'")


class InvalidCurrencyName(ValueError):
    """
    Exception raised when attempting to create a currency with an invalid name.

    :param name: The invalid name of the currency.
    :type name: str
    """

    def __init__(self, name: str):
        super().__init__(f"Invalid currency name: '{name}'\nWhitespace is not allowed in currency names.")

from typing import Union
from .exceptions import InvalidCurrencyName

class Currency:
    """
    Handles everything currency related, including additional metadata.

    Example:

    .. code-block:: python

        # Create a gold currency with 1000 gold and that increase 10 gold each tick
        gold = Currency(name="gold", symbol="G", amount=1000, increment=10)

    :param name: The internal name of the currency, needs to be a valid python variable name.
    :type name: str
    :param amount: The initial amount of the currency, defaults to 0.
    :type amount: Union[int, float]
    :param symbol: The symbol of the currency, this is used when converting the currency to string, defaults to "Gold".
    :type symbol: str
    :param format_str: The format string to format the currency value and symbol when converting into a string. The available parameters are "amount" for the amount of the currency and "symbol" for the symbol of the currency, defaults to "{amount}{symbol}"
    :type format_str: str
    :param increment: The amount by which the currency is increased each tick by the :class:`UUL`, defaults to 1.
    :type increment: Union[int, float]
    :param increment_on_tick: Whether to increment the amount on :class:`UUL` tick, defaults to True.
    :type increment_on_tick: bool
    :raises InvalidCurrencyName: Gets raised if the name contains any white space.
    """

    def __init__(
        self,
        name: str,
        amount: Union[int, float] = 0,
        symbol: str = "G",
        format_str: str = "{amount}{symbol}",
        increment: Union[int, float] = 1,
        increment_on_tick: bool = True
    ):
        if any(char.isspace() for char in name):
            raise InvalidCurrencyName(name)
        self.name = name
        self.amount = amount
        self.symbol = symbol
        self.increment = increment
        self.increment_on_tick = increment_on_tick
        self.format_str = format_str

    def tick(self) -> None:
        """
        Increments the value of the currency by the increment amount.
        
        Example:

        .. code-block:: python

            print(gold) 
            # Output: 1000G
            gold.tick() # Increment the gold currency by 10
            print(gold) 
            # Output: 1010G
        """
        self.amount += self.increment

    def __str__(self) -> str:
        """
        Convert the Currency instance to a formatted string representation.

        The string representation is generated using the format string specified during the Currency's initialization.
        The format string may contain placeholders "{amount}" and "{symbol}" which will be replaced with the amount
        and symbol of the Currency, respectively.

        :return: The string representation of the Currency instance.
        :rtype: str
        """
        return self.format_str.format(amount=self.amount, symbol=self.symbol)

    def __eq__(self, other: Union['Currency', None]) -> bool:
        """
        Check if two Currency instances are equal.
        Two Currency instances are considered equal if their attributes are the same.

        :param other: The other Currency instance to compare.
        :type other: Currency or None
        :return: True if the instances are equal, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, Currency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Union['Currency', None]) -> bool:
        """
        Check if two Currency instances are not equal.

        :param other: The other Currency instance to compare.
        :type other: Currency or None
        :return: True if the instances are not equal, False otherwise.
        :rtype: bool
        """
        return not self.__eq__(other)

    def __lt__(self, other: 'Currency') -> bool:
        """
        Check if the current Currency instance is less than the other Currency instance.
        Comparison is based on the `amount` attribute.

        :param other: The other Currency instance to compare.
        :type other: Currency
        :return: True if the current instance is less than the other instance, False otherwise.
        :rtype: bool
        """
        return self.amount < other.amount

    def __le__(self, other: 'Currency') -> bool:
        """
        Check if the current Currency instance is less than or equal to the other Currency instance.
        Comparison is based on the `amount` attribute.

        :param other: The other Currency instance to compare.
        :type other: Currency
        :return: True if the current instance is less than or equal to the other instance, False otherwise.
        :rtype: bool
        """
        return self.amount <= other.amount

    def __gt__(self, other: 'Currency') -> bool:
        """
        Check if the current Currency instance is greater than the other Currency instance.
        Comparison is based on the `amount` attribute.

        :param other: The other Currency instance to compare.
        :type other: Currency
        :return: True if the current instance is greater than the other instance, False otherwise.
        :rtype: bool
        """
        return self.amount > other.amount

    def __ge__(self, other: 'Currency') -> bool:
        """
        Check if the current Currency instance is greater than or equal to the other Currency instance.
        Comparison is based on the `amount` attribute.

        :param other: The other Currency instance to compare.
        :type other: Currency
        :return: True if the current instance is greater than or equal to the other instance, False otherwise.
        :rtype: bool
        """
        return self.amount >= other.amount


class Currencies:
    """
    An empty container class for managing multiple currencies.
    """
    pass

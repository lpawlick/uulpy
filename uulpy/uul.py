from typing import List, Union
from .currency import Currency, Currencies
from .exceptions import DuplicateCurrencyName

class UUL:
    """
    Universal Upgrade Library (UUL) Object for handling everything related to clicking or upgrading.

    It allows multiple currencies to be handled at once, each represented by a :class:`Currency` object. Each currency can be accessed by its name as the attribute under currencies.

    :param currencies: A list of :class:`Currency` objects or a single :class:`Currency` object to initialize the UUL with.
    :type currencies: Union[List[Currency], Currency]
    :raises DuplicateCurrencyName: Gets raised if two currencies have the same name.

    Example:

    .. code-block:: python
    
        # Create two currencies
        gold = Currency(name="gold", symbol="G", amount=1000, increment=10)
        gems = Currency(name="gems", symbol="💎", amount=50, increment=5, increment_on_tick=False, format_str="{symbol} {amount}")

        # Create a UUL instance with the currencies
        uul = UUL(currencies=[gold, gems])
        print(uul.currencies.gold)  
        # Output: 1000G
        print(uul.currencies.gems)  
        # Output: 💎 50
    """

    def __init__(self, currencies: Union[List[Currency], Currency]):
        self.currencies = Currencies()
        if isinstance(currencies, Currency):
            currencies = [currencies]
        for currency in currencies:
            if hasattr(self.currencies, currency.name):
                raise DuplicateCurrencyName(currency.name)
            setattr(self.currencies, currency.name, currency)

    def tick(self):
        """
        Perform a currency tick to update the values of the currencies.

        This method increments the value of each currency in the UUL instance that has `increment_on_tick` set to True.

        Example:

        .. code-block:: python

            # Perform a currency tick to update the values of all currencies
            uul.tick()
            print(uul.currencies.gold)  
            # Output: 1010G
            print(uul.currencies.gems)  
            # Output: 💎 50
        """
        for currency_name in dir(self.currencies):
            currency = getattr(self.currencies, currency_name)
            if isinstance(currency, Currency) and currency.increment_on_tick:
                currency.tick()

import pytest
from uulpy import Currency
from uulpy.exceptions import InvalidCurrencyName

def test_currency_initialization():
    currency = Currency(name="gold", amount=1000, symbol="G", increment=10)

    assert currency.name == "gold"
    assert currency.amount == 1000
    assert currency.symbol == "G"
    assert currency.increment == 10
    assert currency.increment_on_tick == True
    assert currency.format_str == "{amount}{symbol}"

def test_currency_tick():
    currency = Currency(name="gold", amount=1000, symbol="G", increment=10)

    assert currency.amount == 1000
    currency.tick()
    assert currency.amount == 1010
    currency.tick()
    assert currency.amount == 1020

def test_currency_string_representation():
    currency = Currency(name="gold", amount=1000, symbol="G", increment=10)

    assert str(currency) == "1000G"
    currency.tick()
    assert str(currency) == "1010G"

def test_invalid_currency_name():
    with pytest.raises(InvalidCurrencyName):
        currency = Currency(name="invalid currency name", amount=1000, symbol="G", increment=10)

def test_custom_format_string():
    currency1 = Currency(name="gold", amount=1000, symbol="G", format_str="{amount}{symbol}")
    currency2 = Currency(name="silver", amount=500, symbol="S", format_str="{symbol}-{amount}")

    assert str(currency1) == "1000G"
    assert str(currency2) == "S-500"

def test_negative_increment():
    currency = Currency(name="gold", amount=1000, symbol="G", increment=-10)

    assert currency.amount == 1000
    currency.tick()
    assert currency.amount == 990

def test_float_amount_and_increment():
    currency = Currency(name="gold", amount=1000.5, symbol="G", increment=0.1)

    assert currency.amount == 1000.5
    currency.tick()
    assert currency.amount == 1000.6

def test_currency_equality():
    currency1 = Currency(name="gold", amount=1000, symbol="G", increment=10)
    currency2 = Currency(name="gold", amount=1000, symbol="G", increment=10)
    currency3 = Currency(name="silver", amount=1000, symbol="S", increment=10)

    assert currency1 == currency2
    assert currency1 != currency3
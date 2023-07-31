import pytest
from uulpy import UUL, Currency
from uulpy.exceptions import DuplicateCurrencyName

def test_uul_initialization_with_single_currency():
    gold = Currency(name="gold", symbol="G", amount=1000, increment=10)
    uul = UUL(currencies=gold)

    assert uul.currencies.gold == gold

def test_uul_initialization_with_multiple_currencies():
    gold = Currency(name="gold", symbol="G", amount=1000, increment=10)
    gems = Currency(name="gems", symbol="💎", amount=50, increment=5, increment_on_tick=False, format_str="{symbol} {amount}")
    uul = UUL(currencies=[gold, gems])

    assert uul.currencies.gold == gold
    assert uul.currencies.gems == gems

def test_uul_tick():
    gold = Currency(name="gold", amount=1000, symbol="G", increment=10)
    gems = Currency(name="gems", amount=50, symbol="💎", increment=5, increment_on_tick=False, format_str="{symbol} {amount}")
    uul = UUL(currencies=[gold, gems])

    assert uul.currencies.gold.amount == 1000
    assert uul.currencies.gems.amount == 50

    uul.tick()

    assert uul.currencies.gold.amount == 1010
    assert uul.currencies.gems.amount == 50

    uul.tick()

    assert uul.currencies.gold.amount == 1020
    assert uul.currencies.gems.amount == 50


def test_uul_tick_with_no_currencies():
    uul = UUL(currencies=[])

    # This should not raise an error as there are no currencies to tick
    uul.tick()

def test_uul_with_invalid_currency_names():
    with pytest.raises(AttributeError):
        gold = Currency(name="gold", amount=1000, symbol="G", increment=10)
        uul = UUL(currencies=[gold])
        
        # Try to access an invalid currency name
        invalid_currency = uul.currencies.invalid_name

def test_uul_duplicate_currency_names():
    gold1 = Currency(name="gold", amount=1000, symbol="G", increment=10)
    gold2 = Currency(name="gold", amount=500, symbol="G", increment=5)

    with pytest.raises(DuplicateCurrencyName):
        uul = UUL(currencies=[gold1, gold2])

def test_uul_equality():
    gold1 = Currency(name="gold", amount=1000, symbol="G", increment=10)
    gold2 = Currency(name="gold", amount=1000, symbol="G", increment=10)
    gems = Currency(name="gems", amount=50, symbol="💎", increment=5, increment_on_tick=False, format_str="{symbol} {amount}")
    uul1 = UUL(currencies=[gold1, gems])
    uul2 = UUL(currencies=[gold2, gems])

    assert uul1 != uul2
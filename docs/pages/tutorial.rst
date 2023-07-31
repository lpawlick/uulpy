=========
Tutorial
=========

Creating currencies
--------------------

First we have to create currencies before we can create the main uul Object.

.. code-block:: python

    from uulpy import UUL, Currency
    gold = Currency(name="gold")
    gem = Currency(name="gems", symbol="💎", increment_on_tick=False)

In this example we create two currencies, gold and gems. Gems has a custom symbol and does not increment on a game tick which is created by the UUL object which we will create next.

.. code-block:: python

    uul = UUL(currencies=[gold, gems])
    print(uul.currencies.gems)
    # Output: 0💎

This creates a uul object that manages the currencies and everything else. Currencies can be access under the currencies attribute and are automatically formatted when converted to a string.

Manual Ticks
-------------

A tick represents one unit of time. Advancing the tick will increment the currencies except for the gems currency which we set not to increment on tick.

.. code-block:: python

    uul.tick()
    print(uul.currencies.gold)
    # Output: 1G
    print(uul.currencies.gems)
    # Output: 0💎

The tick method simply advances one tick forward. Currencies that are set not to increment on uul tick can be manually incremented by calling the tick function on the currency.

.. code-block:: python
    
    uul.currencies.gems.tick()
    print(uul.currencies.gems)
    # Output: 1💎

Looking for more?
------------------

Check out the examples in the `examples <https://github.com/lpawlick/uulpy/tree/master/examples>`_ folder.

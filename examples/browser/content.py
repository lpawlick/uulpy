from uulpy import UUL, Currency

uul = UUL(currencies=[Currency(name="usd", format_str="{amount} {symbol}")])

def click():
    uul.tick()
    Element("current-money").write(str(uul.currencies.usd))
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header, Static
from textual import on

from uulpy import UUL, Currency

class Clicker(App):
    CSS_PATH = "uulpy.css"
    BINDINGS = [

    ]

    def __init__(self):
        self.uul = UUL(currencies=[Currency(name="usd", format_str="{amount} {symbol}")])
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container():
            with Container(id="left-tab"):
                yield Button("Click!", id="click", variant="primary")
            yield Static(str(self.uul.currencies.usd), id="show-main-currency")
        yield Footer()

    @on(Button.Pressed, "#click")
    def clicked(self) -> None:
        self.uul.tick()
        self.query_one("#show-main-currency", Static).update(str(self.uul.currencies.usd))

if __name__ == "__main__":
    Clicker().run()

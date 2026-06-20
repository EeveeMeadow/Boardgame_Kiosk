from nicegui import ui
from components import page_header
from regions.base_page import BasePage

example_games = ["Catan", "Shards of infinity", "Brink", "Dune"]

class Homepage(BasePage):

    def create(self) -> None:
        @self.router.page("/")
        def home():
            page_header(example_games)
            with ui.card ():
                ui.label('Boardgame Kiosk')
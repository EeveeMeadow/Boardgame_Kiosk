from nicegui import ui
from components import page_header
from components.catalog import catalog
from regions.base_page import BasePage

example_games = ["Catan", "Shards of infinity", "Brink", "Dune"]

class Homepage(BasePage):
    board_games = {
        'Game 1': {
            'name': 'Catan',
            'players': "2-4",
            'img': 'https://upload.wikimedia.org/wikipedia/en/a/a3/Catan-2015-boxart.jpg',
        },
        'Game 2': {
            'name': 'Brink',
            'players': "2-5",
            'img': 'https://cf.geekdo-images.com/dmFiFjc12CeVWujK5PbVNw__itemrep/img/N1XQfhcOeQniSnOFtfu3JqMVOlQ=/fit-in/246x300/filters:strip_icc()/pic8250385.png'
        },
        'Game 3': {
            'name': 'Dune',
            'players': "2-6",
            'img': 'https://cf.geekdo-images.com/2fgPg6Be--w97zoycObUgg__itemrep/img/R8dZUPLHwkJ4s-4gqdxM529A4w0=/fit-in/246x300/filters:strip_icc()/pic4815198.jpg'
        },
        'Game 4': {
            'name': 'Mystic Vale',
            'players': "2-4",
            'img': 'https://cf.geekdo-images.com/2cf8lebaIrJ8Z62HGEs2wQ__itemrep/img/fHUOINdWuIy88ikjNIVqg-4_Gcw=/fit-in/246x300/filters:strip_icc()/pic3287905.png'
        }
    }

    def create(self) -> None:
        @self.router.page("/")
        def home():
            page_header(self.board_games)
            ui.query('.nicegui-content').classes('absolute-full pt-0')

            with ui.scroll_area().classes('flex-grow'):
                catalog(self.board_games)
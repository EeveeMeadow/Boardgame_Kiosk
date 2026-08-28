from nicegui import ui
from components import page_header, models
from components.bg_catalog import BoardgameSearch
from regions.base_page import BasePage


class Homepage(BasePage):
    def create(self) -> None:
        @self.router.page("/")
        async def home():
            games: list[models.BoardGame] = await models.BoardGame.all()
            page_header()
            ui.query('.nicegui-content').classes('absolute-full pt-0')


            with ui.scroll_area().classes('flex-grow'):
                # catalog(self.board_games)
                await BoardgameSearch(games).populate('')
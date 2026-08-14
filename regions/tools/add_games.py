from nicegui import ui

from components import page_header, models
from components.dialogs.edit_dialog import EditCard
from components.edit_games_page import EditGamesList
from ..base_page import BasePage


class AddGamesPage(BasePage):
    def create(self) -> None:
        @self.router.page('/add_games')
        async def edit_games_page():
            page_header()
            async def create() -> None:
                game = models.BoardGame(name=name.value, owner=0)
                name.value = ''
                game = await EditCard(game).editable_card()
                if not game: return
                await game.save()
                games_list.list_of_games.refresh()

            games_list = EditGamesList()

            with ui.column().classes('mx-auto'):
                with ui.row().classes('w-full items-center px-4'):
                    name = ui.input(label='Name')
                    ui.button(on_click=create, icon='add').props('flat').classes('ml-auto')
                await games_list.list_of_games()

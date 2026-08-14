from nicegui import ui

from components import models
from components.dialogs.edit_dialog import EditCard
from utils.data_utils import decode_db_image


class EditGamesList:

    @ui.refreshable
    async def list_of_games(self) -> None:
        async def delete(game: models.BoardGame) -> None:
            await game.delete()
            self.list_of_games.refresh()

        async def edit(game: models.BoardGame) -> None:
            game = await EditCard(game).editable_card()
            if not game: return
            await game.save()
            self.list_of_games.refresh()

        games: list[models.BoardGame] = await models.BoardGame.all()
        for game in reversed(games):
            with ui.card():
                with ui.row().classes('items-center'):
                    if game.thumbnail:
                        ui.image(decode_db_image(game.thumbnail)).classes('w-20')
                    with ui.grid(columns=2):
                        ui.label('Name')
                        ui.label('Owner')

                        ui.label(game.name)
                        ui.label(game.owner)

                with ui.row().classes('items-center'):
                    ui.button(icon='delete', on_click=lambda u=game: delete(u)).props('flat')
                    ui.button("edit", icon='edit', on_click=lambda u=game: edit(u))
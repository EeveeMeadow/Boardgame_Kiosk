from nicegui import ui

from components import models
from utils.data_utils import decode_db_image


class GameCard:

    def __init__(self, game: models.BoardGame):
        #games: list[models.BoardGame] = await models.BoardGame.all()

        with ui.card().on('click', lambda t=game: self.show_game(t)).classes('w-1/5 min-w-72 max-w-80 '):
            ui.label(game.name)
            if game.thumbnail:
                ui.image(decode_db_image(game.thumbnail)).props('fit=scale-down').classes('h-60')

    # display details of selected game in dialog box
    def show_game(self, game_info: models.BoardGame):
        ui.dialog().clear()
        with ui.dialog() as dialog, ui.card().classes('w-9/12 h-10/12'):
            if game_info.thumbnail:
                ui.image(decode_db_image(game_info.thumbnail)).props('fit=contain').classes('h-4/5')
            ui.label(f'Name: {game_info.name}')
            ui.label(f'Description:\n{game_info.description}').style('white-space: pre-wrap')
        dialog.open()
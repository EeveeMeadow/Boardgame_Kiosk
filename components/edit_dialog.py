from nicegui import ui

from components import models


class EditCard:
    def __init__(self, game: models.BoardGame):
        self.game = game

    def submit(self, dialog: ui.dialog):
        if not self.game.name or self.game.name.isspace():
            ui.notify('Bad Name', type='warning')
            return
        self.game.name = self.game.name.strip()
        dialog.submit(self.game)

    def editable_card(self) -> ui.dialog:
        ui.dialog().clear()
        with ui.dialog() as dialog, ui.card().classes('w-9/12 h-10/12'):
            with ui.grid(columns='auto 1fr').classes('w-full'):
                ui.label('Name:')
                ui.input('Name').bind_value(self.game, 'name').props('item-aligned')

                ui.label('Description:')
                ui.textarea().bind_value(self.game, 'description').classes('w-full')

            with ui.row().classes('items-center'):
                ui.button(icon='save', on_click=lambda: self.submit(dialog)).props('flat')
        return dialog
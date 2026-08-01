from nicegui import ui

class AuditCard:
    def __init__(self, missing_games: list):
        self.mising_games = missing_games

        ui.button('Show Missing Games', on_click=self.show_list)

    def show_list(self):
        ui.dialog().clear()
        with ui.dialog() as dialog, ui.card().classes('w-9/12 h-10/12'):
            for item in self.mising_games:
                ui.label(item['name'])
        dialog.open()
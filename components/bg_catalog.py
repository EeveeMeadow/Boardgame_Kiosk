from nicegui import events, ui


class BoardgameSearch:
    def __init__(self, bg_list):
        self.bg_list = bg_list
        self.search_field = ui.input(placeholder='Search', autocomplete=[x['name'] for x in self.bg_list.values()], on_change=self.search) \
            .props('autofocus outlined rounded item-aligned') \
            .classes('w-96 self-center mt-24 transition-all')
        self.results = ui.row()
        self.populate('')

    def search(self, e: events.ValueChangeEventArguments) -> None:
        self.populate(e.value)

    def show_item(self, game_info):
        ui.dialog().clear()
        with ui.dialog() as dialog, ui.card().classes('w-9/12 h-10/12'):
            ui.image(game_info['img']).props('fit=contain').classes('h-4/5')
            ui.label(f'Name: {game_info['name']}')
            ui.label(f'Players: {game_info['players']}')
        dialog.open()


    def populate(self, search_value: str):
        self.search_field.classes('mt-2', remove='mt-24')
        self.results.clear()
        with self.results:  # enter the context of the results row
            for game in self.bg_list.values():
                if search_value.lower() in game['name'].lower():
                    with ui.card().on('click', lambda t=game: self.show_item(t)).classes('w-1/5 min-w-72 max-w-80 '):
                        ui.label(game['name'])
                        ui.image(game['img']).props('fit=scale-down').classes('h-60')
                        [ui.label(f'{x}: {y}') for x, y in game.items() if x != 'img']

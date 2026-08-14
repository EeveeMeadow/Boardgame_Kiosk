from nicegui import events, ui

from components import models
from components.dialogs.game_card import GameCard


class BoardgameSearch:
    def __init__(self, bg_list: list[models.BoardGame]):
        self.bg_list = bg_list
        self.search_field = ui.input(placeholder='Search', autocomplete=[x.name for x in self.bg_list], on_change=self.search) \
            .props('autofocus outlined rounded item-aligned') \
            .classes('w-96 self-center mt-24 transition-all')
        self.results = ui.row()

    async def search(self, e: events.ValueChangeEventArguments) -> None:
        await self.populate(e.value)


    async def populate(self, search_value: str):

        self.search_field.classes('mt-2', remove='mt-24')
        self.results.clear()
        with self.results:  # enter the context of the results row
            for game in self.bg_list:
                if search_value.lower() in game.name.lower():
                    GameCard(game)


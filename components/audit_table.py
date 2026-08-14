from nicegui import ui

from components import models
from components.dialogs.audit_card import AuditCard


class AuditTable:
    def __init__(self, bg_list: list[models.BoardGame]):
        self.bg_list = bg_list

    def a_table(self):
        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
            {'name': 'location', 'label': 'Location', 'field': 'location', 'sortable': True},
        ]
        rows = []
        for game in self.bg_list:
            rows.append({'id': game.id, 'name': game.name, 'location': 'TBA'})

        with ui.table(title='My Team', columns=columns, rows=rows, selection='multiple', pagination=10).classes(
                'w-96') as table:
            with table.add_slot('top-right'):
                with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                    ui.icon('search')

        ui.label().bind_text_from(table, 'selected', lambda val: f'Current selection: {val}')
        AuditCard(table.selected)
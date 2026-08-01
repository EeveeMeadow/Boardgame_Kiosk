from nicegui import ui



def page_header():

    menu_items = {
        'Audit': '/tools/audit',
        'Add Games' : '/tools/add_games'
    }

    with ui.header(elevated=False).style('background-color: #8243a8').classes('items-center justify-between h-19'):
        ui.label('BoardGame Catalog').on("click",lambda: ui.navigate.to("/")).style("user-select: none").classes('mr-auto')
        with ui.row():
            for title, target in menu_items.items():
                ui.link(title, target).classes(replace='text-lg text-white')

        # ui.input(label='Search', placeholder='Boardgame?', autocomplete=bg_list).props('clearable')
        # ui.select(label="Search", options={k: v["name"] for k, v in bg_list.items()},  with_input=True, clearable=True)
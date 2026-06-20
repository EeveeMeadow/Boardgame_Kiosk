from nicegui import ui



def page_header(bg_list: dict):
    with ui.header(elevated=False).style('background-color: #8243a8').classes('items-center justify-between h-19'):
        ui.label('Boardgame Catalog').style("user-select: none").classes('mr-auto')

        # ui.input(label='Search', placeholder='Boardgame?', autocomplete=bg_list).props('clearable')
        ui.select(label="Search", options={k: v["name"] for k, v in bg_list.items()},  with_input=True, clearable=True)
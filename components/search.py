

from nicegui import events, ui


board_games = {
        'Game 1': {
            'name': 'Catan',
            'players': "2-4",
            'img': 'https://upload.wikimedia.org/wikipedia/en/a/a3/Catan-2015-boxart.jpg',
        },
        'Game 2': {
            'name': 'Brink',
            'players': "2-5",
            'img': 'https://cf.geekdo-images.com/dmFiFjc12CeVWujK5PbVNw__itemrep/img/N1XQfhcOeQniSnOFtfu3JqMVOlQ=/fit-in/246x300/filters:strip_icc()/pic8250385.png'
        },
        'Game 3': {
            'name': 'Dune',
            'players': "2-6",
            'img': 'https://cf.geekdo-images.com/2fgPg6Be--w97zoycObUgg__itemrep/img/R8dZUPLHwkJ4s-4gqdxM529A4w0=/fit-in/246x300/filters:strip_icc()/pic4815198.jpg'
        },
        'Game 4': {
            'name': 'Mystic Vale',
            'players': "2-4",
            'img': 'https://cf.geekdo-images.com/2cf8lebaIrJ8Z62HGEs2wQ__itemrep/img/fHUOINdWuIy88ikjNIVqg-4_Gcw=/fit-in/246x300/filters:strip_icc()/pic3287905.png'
        }
    }




def search(e: events.ValueChangeEventArguments) -> None:
    populate(e.value)

def populate(search_value: str):
    search_field.classes('mt-2', remove='mt-24')
    results.clear()
    with results:  # enter the context of the results row
        for game in board_games.values():  # iterate over the response data of the api
            if search_value.lower() in game['name'].lower():
                with ui.image(game['img']).classes('w-64'):
                    ui.label(game['name']).classes('absolute-bottom text-subtitle2 text-center')



# create a search field which is initially focused and leaves space at the top
search_field = ui.input(on_change=search) \
    .props('autofocus outlined rounded item-aligned input-class="ml-3"') \
    .classes('w-96 self-center mt-24 transition-all')
results = ui.row()
populate('')

ui.run()
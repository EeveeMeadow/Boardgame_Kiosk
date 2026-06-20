from nicegui import ui

def catalog(catalog_item: dict[str, dict[str, str]]):
    #this Creates a function to replace what ever the current dialog box says with new information.

    def show_item(name):
        ui.dialog().clear()
        with ui.dialog() as dialog, ui.card():
            ui.label(name)
        dialog.open()

    with ui.row().classes('w-full gap-5 justify-center'):
        for i in range(20): #this for loop is temporary and will be removed when we have a DB with all Items

            #creates a card for each item in the dictionary and populates it with all dictionary items
            for title, data in catalog_item.items():
                with ui.card().on('click', lambda t=title: show_item(t)).classes('w-1/5 min-w-72 max-w-80'):
                    ui.label(title)
                    ui.image(data['img'])
                    [ui.label(f'{x}: {y}') for x, y in data.items() if x != 'img']

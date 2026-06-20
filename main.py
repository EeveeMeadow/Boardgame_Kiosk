from nicegui import ui, app

from regions import BaseRouter



app.include_router(BaseRouter)


ui.run(dark=True, title="Boardgame Kiosk")
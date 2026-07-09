from nicegui import ui, app

from regions import BaseRouter
from regions import ToolRouter

app.include_router(BaseRouter)
app.include_router(ToolRouter)


ui.run(dark=True, title="Boardgame Kiosk")
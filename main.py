from nicegui import ui, app
from tortoise import TortoiseConfig
from tortoise.config import DBUrlConfig, AppConfig
from tortoise.contrib.fastapi import register_tortoise

from regions import BaseRouter
from regions import ToolRouter

register_tortoise(
        app,
        config=TortoiseConfig(
            use_tz=True,
            timezone='UTC',
            connections={'default': DBUrlConfig(url='postgres://eveya:AryaLovesEve@192.168.1.51:31854/boardgames')},
            apps={'models': AppConfig(models=['components.models'])}
        )
    )

app.include_router(BaseRouter)
app.include_router(ToolRouter)


ui.run(dark=True, title="Boardgame Kiosk")
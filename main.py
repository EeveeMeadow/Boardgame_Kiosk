from os import getenv

from dotenv import load_dotenv
from nicegui import ui, app
from tortoise import TortoiseConfig
from tortoise.config import DBUrlConfig, AppConfig
from tortoise.contrib.fastapi import register_tortoise

from regions import BaseRouter 
from regions import ToolRouter

# load enviroment variables.
load_dotenv()
pg_user = getenv("PG_USER")
pg_password = getenv("PG_PASS")
pg_host = getenv("PG_HOST")
pg_port = getenv("PG_PORT")
pg_db = getenv("PG_DB")

#load database access
register_tortoise(
        app,
        config=TortoiseConfig(
            use_tz=True,
            timezone='UTC',
            connections={'default': DBUrlConfig(url=f'postgres://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')},
            apps={'models': AppConfig(models=['components.models'])}
        )
    )

app.include_router(BaseRouter)
app.include_router(ToolRouter)


ui.run(dark=True, title="Boardgame Kiosk")
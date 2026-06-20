from nicegui import APIRouter

from regions.home import Homepage


BaseRouter= APIRouter()
Homepage(BaseRouter)

__all__ = ['BaseRouter']
from nicegui import APIRouter

from regions.home import Homepage
from regions.tools import ToolRouter

BaseRouter = APIRouter()
Homepage(BaseRouter)

__all__ = ['BaseRouter', 'ToolRouter']
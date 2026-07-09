from nicegui import APIRouter

from .add_games import AddGamesPage
from .audit_page import AuditPage


ToolRouter = APIRouter(prefix="/tools")
AuditPage(ToolRouter)
AddGamesPage(ToolRouter)


__all__ = ['ToolRouter']
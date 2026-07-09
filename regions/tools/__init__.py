from nicegui import APIRouter

from .audit_page import AuditPage


ToolRouter = APIRouter(prefix="/tools")
AuditPage(ToolRouter)

__all__ = ['ToolRouter']
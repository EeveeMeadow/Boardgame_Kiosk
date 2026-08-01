from nicegui import ui

from components import page_header, models
from components.audit_table import AuditTable
from regions.base_page import BasePage


class AuditPage(BasePage):
    def create(self) -> None:
        @self.router.page('/audit')
        async def audit_page():
            games: list[models.BoardGame] = await models.BoardGame.all()
            page_header()
            ui.query('.nicegui-content').classes('absolute-full pt-0')
            AuditTable(games).a_table()
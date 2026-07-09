from nicegui import ui

from components import page_header
from ..base_page import BasePage


class AuditPage(BasePage):
    def create(self) -> None:
        @self.router.page('/audit')
        def audit_page():
            page_header()
            with ui.card():
                ui.label("This is a temporary test page")
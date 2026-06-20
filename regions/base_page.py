from abc import ABC, abstractmethod

from nicegui import APIRouter


class BasePage(ABC):
    def __init__(self, router: APIRouter):
        self.router = router
        self.create()

    @abstractmethod
    def create(self) -> None:
        pass
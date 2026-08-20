from PySide6.QtWidgets import (
    QStackedWidget,
    QLabel,
    QWidget,
    QVBoxLayout,
)

from ui.pages.create_presentation_page import CreatePresentationPage
from ui.pages.settings_page import SettingsPage


class ContentWidget(QStackedWidget):

    def __init__(self, worker_manager, parent=None):
        super().__init__(parent)

        self.worker_manager = worker_manager

        self.pages = {}

        self._create_pages()

    def _create_pages(self):
        self._add_page(
            "home",
            self._create_test_page("Головна"),
        )

        self._add_page(
            "create",
            CreatePresentationPage(
                self.worker_manager
            )
        )

        self._add_page(
            "presentations",
            self._create_test_page("Презентації"),
        )

        self._add_page(
            "files",
            self._create_test_page("Налаштування файлів"),
        )

        self._add_page(
            "settings",
            SettingsPage(),
        )

    def _add_page(self, name, page):
        self.addWidget(page)
        self.pages[name] = page

    def _create_test_page(self, title):
        from PySide6.QtWidgets import QLabel

        return QLabel(title)

    def set_page(self, name: str):
        page = self.pages.get(name)

        if page is None:
            return

        self.setCurrentWidget(page)

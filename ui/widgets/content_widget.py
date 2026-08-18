from PySide6.QtWidgets import (
    QStackedWidget,
    QLabel,
    QWidget,
    QVBoxLayout,
)

from ui.pages.create_presentation_page import CreatePresentationPage


class ContentWidget(QStackedWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pages = {}

        self._create_pages()

    def _create_pages(self):
        self._add_page(
            "home",
            self._create_test_page("Головна"),
        )

        self._add_page(
            "create",
            CreatePresentationPage(),
        )

        self._add_page(
            "presentations",
            self._create_test_page("Презентації"),
        )

        self._add_page(
            "ai",
            self._create_test_page("Налаштування AI"),
        )

        self._add_page(
            "files",
            self._create_test_page("Налаштування файлів"),
        )

        self._add_page(
            "settings",
            self._create_test_page("Налаштування"),
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

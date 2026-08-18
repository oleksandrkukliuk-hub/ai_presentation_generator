from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
)


class NavigationBar(QFrame):

    page_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("navigation_bar")

        self._create_ui()
        self._connect_signals()

    def _create_ui(self):
        layout = QHBoxLayout(self)

        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(6)

        self.home_button = self._create_button("Головна")
        self.create_button = self._create_button("Створити презентацію")
        self.presentations_button = self._create_button("Презентації")

        self.files_button = self._create_button("Файли")
        self.settings_button = self._create_button("Налаштування")

        layout.addWidget(self.home_button)
        layout.addWidget(self.create_button)
        layout.addWidget(self.presentations_button)
        layout.addWidget(self.files_button)
        layout.addWidget(self.settings_button)
        layout.addStretch()

    def _create_button(self, text: str) -> QPushButton:
        button = QPushButton(text)

        button.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        return button

    def _connect_signals(self):
        self.home_button.clicked.connect(
            lambda: self.page_changed.emit("home")
        )

        self.create_button.clicked.connect(
            lambda: self.page_changed.emit("create")
        )

        self.presentations_button.clicked.connect(
            lambda: self.page_changed.emit("presentations")
        )

        self.files_button.clicked.connect(
            lambda: self.page_changed.emit("files")
        )

        self.settings_button.clicked.connect(
            lambda: self.page_changed.emit("settings")
        )

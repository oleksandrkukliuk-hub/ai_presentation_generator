from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout

from ui.widgets.content_widget import ContentWidget
from ui.widgets.navigation_bar import NavigationBar
from ui.workers.worker_manager import WorkerManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Presentation Generator")
        self.resize(1200, 800)

        self.worker_manager = WorkerManager(self)

        self._create_ui()
        self._connect_signals()


    def _create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.navigation_bar = NavigationBar()
        self.content = ContentWidget(self.worker_manager)

        main_layout.addWidget(self.navigation_bar)
        main_layout.addWidget(self.content, 1)

    def _connect_signals(self):
        self.navigation_bar.page_changed.connect(
            self.content.set_page
        )

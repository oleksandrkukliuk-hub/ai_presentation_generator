import time

from PySide6.QtCore import QObject, Signal, Slot


class PresentationWorker(QObject):
    finished = Signal()
    error = Signal(str)

    progress = Signal(int)
    status = Signal(str)

    result = Signal(str)

    def __init__(self, data):
        super().__init__()

        self.data = data

    @Slot()
    def run(self):
        try:
            self.status.emit("Підготовка...")
            self.progress.emit(10)

            self.progress.emit(100)
            time.sleep(0.7)


            self.status.emit("Готово")
            self.result.emit(str(self.data))

            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))

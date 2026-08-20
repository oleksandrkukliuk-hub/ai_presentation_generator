import time

from PySide6.QtCore import QObject, Signal, Slot


class PresentationWorker(QObject):
    finished = Signal()
    error = Signal(str)

    progress = Signal(int)
    status = Signal(str)

    def __init__(self, data):
        super().__init__()

        self.data = data

    @Slot()
    def run(self):
        try:
            self.status.emit("Підготовка...")
            self.progress.emit(10)

            time.sleep(1)

            self.status.emit("Генеруємо текст...")
            self.progress.emit(30)

            time.sleep(1)

            self.status.emit("Створюємо структуру...")
            self.progress.emit(60)

            time.sleep(1)

            self.status.emit("Створюємо слайди...")
            self.progress.emit(90)

            time.sleep(1)



            self.progress.emit(100)
            time.sleep(0.7)

            print(self.data)
            self.status.emit("Готово")

            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))
from PySide6.QtCore import QObject, QThread, Signal


class WorkerManager(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._threads = []
        self._workers = []

    def run(self, worker):
        thread = QThread()

        self._threads.append(thread)
        self._workers.append(worker)

        worker.moveToThread(thread)

        thread.started.connect(worker.run)

        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)

        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        thread.finished.connect(
            lambda: self._cleanup(thread, worker)
        )

        thread.start()

    def _cleanup(self, thread, worker):
        if thread in self._threads:
            self._threads.remove(thread)

        if worker in self._workers:
            self._workers.remove(worker)
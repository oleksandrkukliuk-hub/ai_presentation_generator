import time

from PySide6.QtCore import QObject, Signal, Slot

from schemas.lesson_content import LessonContent


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

            print(self.data)

            lesson = LessonContent.model_validate({
  "lesson_topic": "Фізика — наука про природу. Фізичні тіла та фізичні явища.",
  "class": "7 клас",
  "academic_subject": "Фізика",
  "lesson_type": "Вивчення нової теми",
  "slides": [
    {
      "slide_number": 1,
      "title": "Фізика — наука про природу",
      "text": "Фізика вивчає властивості тіл, явища природи та закономірності, за якими вони відбуваються.",
      "purpose": "Мотивація та введення в тему"
    },
    {
      "slide_number": 2,
      "title": "Що таке фізичне тіло?",
      "text": "Фізичне тіло — це будь-який предмет, який має форму, об'єм та інші фізичні властивості.",
      "examples": [
        "м'яч",
        "автомобіль",
        "склянка",
        "камінь"
      ],
      "purpose": "Сформувати поняття фізичного тіла"
    },
    {
      "slide_number": 3,
      "title": "Фізичні явища",
      "text": "Фізичне явище — це зміна, яка відбувається з фізичним тілом або в природі.",
      "examples": [
        "рух автомобіля",
        "танення льоду",
        "поширення звуку"
      ],
      "purpose": "Сформувати поняття фізичного явища"
    }
  ]
})

            print(lesson)

            self.progress.emit(100)
            time.sleep(0.7)

            self.status.emit("Готово")
            self.result.emit(str(self.data))

            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))

from PySide6.QtCore import QThread
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QComboBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from ui.workers.presentation_worker import PresentationWorker
from PySide6.QtCore import QPropertyAnimation, QEasingCurve


class CreatePresentationPage(QWidget):
    def __init__(self, worker_manager, parent=None):
        super().__init__(parent)

        self.worker_manager = worker_manager

        self._create_ui()

        self.progress_animation = QPropertyAnimation(
            self.progress_bar,
            b"value"
        )

        self.progress_animation.setDuration(700)
        self.progress_animation.setEasingCurve(
            QEasingCurve.Type.InOutQuad
        )
        self.generate_button.clicked.connect(
            self._generate_presentation
        )

    def _create_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # ==========================================
        # Верхня частина
        # ==========================================

        content_layout = QHBoxLayout()
        content_layout.setSpacing(10)

        # ------------------------------------------
        # Frame з параметрами
        # ------------------------------------------

        self.input_frame = QFrame()
        self.input_frame.setFrameShape(QFrame.Shape.StyledPanel)

        input_layout = QVBoxLayout(self.input_frame)

        title_label = QLabel("Параметри презентації")

        input_layout.addWidget(title_label)

        # Клас
        input_layout.addWidget(QLabel("Клас"))

        self.grade_combo = QComboBox()
        self.grade_combo.addItems([
            "5 клас",
            "6 клас",
            "7 клас",
            "8 клас",
            "9 клас",
            "10 клас",
            "11 клас",
        ])

        input_layout.addWidget(self.grade_combo)

        # Тип уроку
        input_layout.addWidget(QLabel("Тип уроку"))

        self.lesson_type_combo = QComboBox()
        self.lesson_type_combo.addItems([
            "Вивчення нової теми",
            "Закріплення вивченого матеріалу",
            "Розв'язування задач",
            "Практична робота",
            "Лабораторна робота",
            "Контрольна робота",
            "Самостійна робота",
            "Узагальнення та систематизація знань",
            "Повторення матеріалу",
            "Комбінований урок",
            "Інше",
        ])

        input_layout.addWidget(self.lesson_type_combo)

        # Предмет
        input_layout.addWidget(QLabel("Предмет"))

        self.subject_combo = QComboBox()
        self.subject_combo.addItems([
            "Математика",
            "Фізика",
            "Інформатика",
            "Хімія",
            "Біологія",
            "Історія",
        ])

        input_layout.addWidget(self.subject_combo)

        # Тема
        input_layout.addWidget(QLabel("Тема"))

        self.topic_edit = QLineEdit()
        self.topic_edit.setPlaceholderText(
            "Введіть тему уроку..."
        )

        input_layout.addWidget(self.topic_edit)

        # Додаткова інформація
        input_layout.addWidget(
            QLabel("Додаткові інструкції для ШІ")
        )

        self.additional_instructions_edit = QTextEdit()
        self.additional_instructions_edit.setPlaceholderText(
            "Наприклад: додати практичні завдання, "
            "експерименти, більше ілюстрацій..."
        )

        input_layout.addWidget(
            self.additional_instructions_edit
        )

        # input_layout.addStretch()

        # ------------------------------------------
        # Frame з preview
        # ------------------------------------------

        self.preview_frame = QFrame()
        self.preview_frame.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        preview_layout = QVBoxLayout(
            self.preview_frame
        )

        preview_title = QLabel(
            "Передперегляд презентації"
        )

        preview_layout.addWidget(preview_title)

        self.preview_label = QLabel(
            "Передперегляд буде доступний "
            "після створення презентації."
        )

        self.preview_label.setWordWrap(True)

        preview_layout.addWidget(
            self.preview_label
        )

        preview_layout.addStretch()

        # ------------------------------------------
        # Додаємо верхні Frame
        # ------------------------------------------

        content_layout.addWidget(
            self.input_frame,
            1,
        )

        content_layout.addWidget(
            self.preview_frame,
            3,
        )

        main_layout.addLayout(
            content_layout,
            1,
        )

        # ==========================================
        # Нижній Frame
        # ==========================================

        self.status_frame = QFrame()
        self.status_frame.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        status_layout = QVBoxLayout(
            self.status_frame
        )

        # Верхній рядок статусу
        status_top_layout = QHBoxLayout()

        self.status_label = QLabel(
            "Готово до створення презентації"
        )

        self.generate_button = QPushButton(
            "Генерувати"
        )

        status_top_layout.addWidget(
            self.status_label
        )

        status_top_layout.addStretch()

        status_top_layout.addWidget(
            self.generate_button
        )

        status_layout.addLayout(
            status_top_layout
        )

        # Progress bar
        self.progress_bar = QProgressBar()

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        status_layout.addWidget(
            self.progress_bar
        )

        main_layout.addWidget(
            self.status_frame
        )

    def _generate_presentation(self):
        data = {
            "class": self.grade_combo.currentText(),
            "academic_subject": self.subject_combo.currentText(),
            "lesson_type": self.lesson_type_combo.currentText(),
            "lesson_topic": self.topic_edit.text(),
            "additional_instructions": (
                self.additional_instructions_edit.toPlainText()
            ),
        }

        self.progress_bar.setValue(0)

        worker = PresentationWorker(data)

        worker.progress.connect(
            self._update_progress
        )

        worker.status.connect(
            self.status_label.setText
        )

        worker.result.connect(
            self.preview_label.setText
        )

        worker.finished.connect(
            self._generation_finished
        )

        worker.error.connect(
            self._generation_error
        )

        self.generate_button.setEnabled(False)

        self.worker_manager.run(worker)

    def _generation_finished(self):
        self.status_label.setText(
            "Презентацію створено"
        )

        self.generate_button.setEnabled(True)

    def _generation_error(self, message):
        self.status_label.setText(
            f"Помилка: {message}"
        )

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

    def _update_progress(self, value):
        self.progress_animation.stop()

        self.progress_animation.setStartValue(
            self.progress_bar.value()
        )

        self.progress_animation.setEndValue(value)

        self.progress_animation.start()

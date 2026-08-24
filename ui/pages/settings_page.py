from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget, QHBoxLayout,
)

from config.settings import settings

AI_MODELS = dict(settings.AI_MODELS)

AI_PROVIDERS = list(AI_MODELS.keys())


class SettingsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._create_ui()

    def _create_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        title = QLabel("Налаштування")

        main_layout.addWidget(title)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(
            QFrame.Shape.NoFrame
        )

        scroll_widget = QWidget()

        scroll_layout = QVBoxLayout(scroll_widget)

        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(10)

        self._add_ai_frame(scroll_layout)
        self._add_interface_frame(scroll_layout)

        scroll_layout.addStretch()

        scroll_area.setWidget(
            scroll_widget
        )

        main_layout.addWidget(
            scroll_area,
            1,
        )

        self.save_button = QPushButton(
            "Зберегти"
        )

        main_layout.addWidget(
            self.save_button
        )

    def _add_interface_frame(self, scroll_layout):
        interface_frame = QFrame()

        interface_frame.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        interface_layout = QVBoxLayout(
            interface_frame
        )

        interface_title = QLabel(
            "Інтерфейс"
        )

        interface_layout.addWidget(
            interface_title
        )

        # Мова
        interface_layout.addWidget(
            QLabel("Мова")
        )

        self.language_combo = QComboBox()

        self.language_combo.addItems([
            "Українська",
            "English",
        ])

        interface_layout.addWidget(
            self.language_combo
        )

        # Тема
        interface_layout.addWidget(
            QLabel("Тема")
        )

        self.theme_combo = QComboBox()

        self.theme_combo.addItems([
            "Системна",
            "Світла",
            "Темна",
        ])

        interface_layout.addWidget(
            self.theme_combo
        )

        scroll_layout.addWidget(
            interface_frame
        )

    def _add_ai_frame(self, scroll_layout):
        ai_frame = QFrame()

        ai_frame.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        ai_layout = QVBoxLayout(ai_frame)

        ai_layout.addWidget(QLabel("AI"))

        providers_layout = QHBoxLayout()
        providers_layout.setSpacing(10)

        ai_layout.addLayout(providers_layout)

        text_ai_frame = QFrame()
        text_ai_frame.setFrameShape(QFrame.Shape.StyledPanel)

        text_ai_layout = QVBoxLayout(text_ai_frame)

        text_ai_layout.addWidget(
            QLabel("Генерація тексту")
        )

        text_ai_layout.addWidget(
            QLabel("Провайдер")
        )

        text_ai_provider = settings.AI.ai_content_generator.provider

        self.text_ai_provider_combo = QComboBox()
        self.text_ai_provider_combo.addItems(AI_PROVIDERS)
        self.text_ai_provider_combo.setCurrentText(text_ai_provider)

        self.text_ai_provider_combo.currentTextChanged.connect(
            self._text_ai_update_models
        )

        text_ai_layout.addWidget(
            self.text_ai_provider_combo
        )

        text_ai_layout.addWidget(
            QLabel("Модель")
        )

        self.text_ai_model_combo = QComboBox()
        self.text_ai_model_combo.addItems(AI_MODELS[text_ai_provider])
        self.text_ai_model_combo.setCurrentText(settings.AI.ai_content_generator.model)
        self.text_ai_model_combo.currentTextChanged.connect(
            self._text_ai_set_model
        )

        text_ai_layout.addWidget(
            self.text_ai_model_combo
        )

        text_ai_layout.addWidget(
            QLabel("API ключ")
        )

        text_ai_api_key = settings.AI.ai_content_generator.api_key

        self.text_ai_api_key_edit = QLineEdit()
        self.text_ai_api_key_edit.setPlaceholderText(
            "Введіть API ключ..."
        )
        self.text_ai_api_key_edit.setText(text_ai_api_key)
        self.text_ai_api_key_edit.textChanged.connect(self._text_api_key_changed)

        self.text_ai_api_key_edit.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        text_ai_layout.addWidget(
            self.text_ai_api_key_edit
        )

        self.text_ai_check_button = QPushButton(
            "Перевірити підключення"
        )

        text_ai_layout.addWidget(
            self.text_ai_check_button
        )

        json_ai_frame = QFrame()
        json_ai_frame.setFrameShape(QFrame.Shape.StyledPanel)

        json_ai_layout = QVBoxLayout(json_ai_frame)

        json_ai_layout.addWidget(
            QLabel("Генерація структури")
        )

        json_ai_layout.addWidget(
            QLabel("Провайдер")
        )

        json_ai_provider = settings.AI.ai_slide_renderer.provider

        self.json_ai_provider_combo = QComboBox()
        self.json_ai_provider_combo.addItems(AI_PROVIDERS)
        self.json_ai_provider_combo.setCurrentText(json_ai_provider)

        self.json_ai_provider_combo.currentTextChanged.connect(
            self._json_ai_update_models
        )

        json_ai_layout.addWidget(
            self.json_ai_provider_combo
        )

        json_ai_layout.addWidget(
            QLabel("Модель")
        )

        self.json_ai_model_combo = QComboBox()
        self.json_ai_model_combo.addItems(AI_MODELS[json_ai_provider])
        self.json_ai_model_combo.setCurrentText(settings.AI.ai_slide_renderer.model)
        self.json_ai_model_combo.currentTextChanged.connect(
            self._json_ai_set_model
        )

        json_ai_layout.addWidget(
            self.json_ai_model_combo
        )

        json_ai_layout.addWidget(
            QLabel("API ключ")
        )

        json_ai_api_key = settings.AI.ai_slide_renderer.api_key

        self.json_ai_api_key_edit = QLineEdit()
        self.json_ai_api_key_edit.setPlaceholderText(
            "Введіть API ключ..."
        )
        self.json_ai_api_key_edit.setText(json_ai_api_key)
        self.json_ai_api_key_edit.textChanged.connect(self._json_api_key_changed)

        self.json_ai_api_key_edit.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        json_ai_layout.addWidget(
            self.json_ai_api_key_edit
        )

        self.json_ai_check_button = QPushButton(
            "Перевірити підключення"
        )

        json_ai_layout.addWidget(
            self.json_ai_check_button
        )

        providers_layout.addWidget(
            text_ai_frame,
            1,
        )

        providers_layout.addWidget(
            json_ai_frame,
            1,
        )

        scroll_layout.addWidget(
            ai_frame
        )

    def _text_api_key_changed(self, text):
        settings.AI.ai_content_generator.api_key = text

    def _json_api_key_changed(self, text):
        settings.AI.ai_slide_renderer.api_key = text

    @staticmethod
    def _update_models(provider, instance):
        instance.clear()
        instance.addItems(
            AI_MODELS.get(provider, [])
        )

    def _text_ai_update_models(self, provider):
        self._update_models(provider, self.text_ai_model_combo)
        settings.AI.ai_content_generator.provider = provider
        settings.AI.ai_content_generator.model = self.text_ai_model_combo.currentText()

    def _json_ai_update_models(self, provider):
        self._update_models(provider, self.json_ai_model_combo)
        settings.AI.ai_slide_renderer.provider = provider
        settings.AI.ai_slide_renderer.model = self.json_ai_model_combo.currentText()

    @staticmethod
    def _text_ai_set_model(model):
        settings.AI.ai_content_generator.model = model

    @staticmethod
    def _json_ai_set_model(model):
        settings.AI.ai_slide_renderer.model = model


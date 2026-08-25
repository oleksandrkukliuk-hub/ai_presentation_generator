from pydantic import BaseModel, Field


class SlideContent(BaseModel):
    slide_number: int = Field(
        description="Порядковий номер слайда"
    )
    title: str = Field(
        description="Заголовок слайда"
    )
    text: str = Field(
        description="Основний текст слайда"
    )
    purpose: str = Field(
        description="Педагогічна мета слайда"
    )
    examples: list[str] = Field(
        default_factory=list,
        description="Приклади, які потрібно навести на слайді"
    )


class LessonContent(BaseModel):
    lesson_topic: str = Field(
        description="Тема уроку"
    )
    class_: str = Field(
        alias="class",
        description="Клас учнів"
    )
    academic_subject: str = Field(
        description="Навчальний предмет"
    )
    lesson_type: str = Field(
        description="Тип уроку"
    )
    slides: list[SlideContent] = Field(
        description="Список слайдів презентації"
    )
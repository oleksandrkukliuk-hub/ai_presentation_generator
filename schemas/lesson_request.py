from pydantic import BaseModel, Field


class LessonRequest(BaseModel):
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
    lesson_topic: str = Field(
        description="Тема уроку"
    )
    additional_instructions: str = Field(
        default="",
        description="Додаткова інструкція для генерації слайдів"
    )
    prompt: str = Field(
        default="",
        description="Додаткові побажання до генерації"
    )

    model_config = {
        "populate_by_name": True,
        "extra": "forbid",
    }
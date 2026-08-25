import json
from typing import Type, TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel

from schemas.lesson_content import LessonContent
from base import BaseAIClient

T = TypeVar("T", bound=BaseModel)


class GeminiClient(BaseAIClient):

    def __init__(
            self,
            api_key: str,
            model: str,
    ):
        self.client = genai.Client(
            api_key=api_key
        )
        self.model = model

    def generate(
            self,
            prompt: str,
            response_schema: Type[T],
    ) -> T:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            ),
        )

        return response.parsed

if __name__ == "__main__":
    client = GeminiClient(
        api_key="",
        model="gemini-3.6-flash",
    )
    result = client.generate(
        prompt="Створи якісну презентацію на 10 слайдів для учнів 9 класу з фізики на тему 'Закон Ома'",
        response_schema=LessonContent,
    )

    print(
        json.dumps(
            result.model_dump(),
            ensure_ascii=False,
            indent=4,
        )
    )

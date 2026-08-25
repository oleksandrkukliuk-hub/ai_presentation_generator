from abc import ABC, abstractmethod

from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseAIClient(ABC):

    @abstractmethod
    def generate(
            self,
            prompt: str,
            response_schema: Type[T],
    ) -> T:
        """
        Надсилає prompt до AI та повертає
        необроблений текст відповіді.
        """
        raise NotImplementedError

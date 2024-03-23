from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TextTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"text message is too long '{self.text[:255]}...'"


@dataclass(eq=False)
class EmptyTextError(ApplicationException):
    text: str

    @property
    def message(self):
        return "the text cannot be empty"

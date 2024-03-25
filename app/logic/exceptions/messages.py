from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class ChatWithThatTitleAlreadyExistException(LogicException):
    title: str

    @property
    def message(self):
        return f"Чат с таким названием '{self.title}' уже существует."

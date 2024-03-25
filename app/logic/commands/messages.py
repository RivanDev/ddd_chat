from dataclasses import dataclass

from domain.entities.messages import Chat
from logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand]):
    chat_repository: BaseChatRepository

    def handle(self, command: CreateChatCommand) -> Chat:
        if self.chat_repository.check_chat_exist_by_title(command.title):
            raise ChatWithThatTitleAlreadyExistException(command.title)

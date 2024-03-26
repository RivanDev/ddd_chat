import pytest
from faker import Faker

from domain.entities.messages import Chat
from domain.values.messages import Title
from infra.repositories.messages import BaseChatRepository
from logic.commands.messages import CreateChatCommand
from logic.exceptions.messages import ChatWithThatTitleAlreadyExistException
from logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_chat_command_success(
    chat_repository: BaseChatRepository,
    mediator: Mediator,
    faker: Faker,
):
    chat: Chat = (await mediator.handle_command(CreateChatCommand(title=faker.text())))[
        0
    ]

    assert await chat_repository.check_chat_exist_by_title(
        title=chat.title.as_generic_type()
    )


@pytest.mark.asyncio
async def test_create_chat_command_title_already_exist(
    chat_repository: BaseChatRepository,
    mediator: Mediator,
    faker: Faker,
):
    chat = Chat(title=Title(faker.text()))
    await chat_repository.add_chat(chat)
    with pytest.raises(ChatWithThatTitleAlreadyExistException):
        await mediator.handle_command(CreateChatCommand(title=faker.text()))

    assert await len(chat_repository._saved_chats) == 1

from datetime import datetime

import pytest

from domain.entities.messages import Message, Chat
from domain.exceptions.messages import TitleTooLongException
from domain.values.messages import Text, Title


def test_create_message_success():
    text = Text("Hello word")
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_chat_too_long_title():
    with pytest.raises(TitleTooLongException):
        Title("title" * 200)


def test_create_chat_success():
    title = Title("title")
    chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


def test_add_message_to_chat():
    text = Text("Hello word")
    message = Message(text=text)

    title = Title("title")
    chat = Chat(title=title)

    chat.add_message(message)
    assert message in chat.messages

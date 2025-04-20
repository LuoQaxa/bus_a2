import pytest
from chatroom import ChatRoom
from user import Student
from notification import PersonalisedNotification

# Positive test case
def test_chatroom_positive():
    # Create a chat room
    chat_room = ChatRoom("BUS")
    assert chat_room.name == "BUS"
    assert len(chat_room.users) == 0

    # Create users
    notification_system = PersonalisedNotification()
    alice = Student("Alice", "1234567890", notification_system)

    # User joins the chat room
    chat_room.join_chatroom(alice)
    assert len(chat_room.users) == 1
    assert alice in chat_room.users

    # Broadcast a message
    chat_room.broadcast(alice, "Hello, everyone!")
    assert len(chat_room.messages) == 1
    assert chat_room.messages[0]['sender'].name == 'Alice'
    assert chat_room.messages[0]['content'] == "Hello, everyone!"

    # User leaves the chat room
    chat_room.remove_user(alice)
    assert len(chat_room.users) == 0

# Negative test case
def test_chatroom_negative():
    # Create a chat room
    chat_room = ChatRoom("BUS")

    # Create a user
    notification_system = PersonalisedNotification()

    # Remove a non-existent user
    with pytest.raises(ValueError):
        chat_room.remove_user(Student("NonExistent", "9999999999", notification_system))
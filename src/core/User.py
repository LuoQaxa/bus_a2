import chatroom
class User():
    def __init__(self, name):
        self.name = name

class Student(User):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.chatroom = None

    def create_chatroom(self, name):
        chat_room = chatroom.ChatRoom(name)
        self.join_chatroom(chat_room)
        self.chatroom = chat_room
        return chat_room

    def join_chatroom(self, room):
        if self.chatroom:
            print(f"{self.name} has already joined another chatroom")
            return
        room.add_user(self)

    def send_message(self, content):
        if self.chatroom:
            self.chatroom.broadcast(self, content)
        else:
            print("Please join a chatroom first")

    def leave_chatroom(self):
        if self.chatroom:
            self.chatroom.remove_user(self)
            self.chatroom = None
            print(f"{self.name} has left the chatroom")


class Staff(User):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id
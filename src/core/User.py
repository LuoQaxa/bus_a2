import chatroom
from notification import Dashboard

class User():
    def __init__(self, name):
        self.name = name

    # Add method - to say if someone can post or not - with references to class diagram
    def canPostAnnouncement(self):
        return False

class Student(User):
    def __init__(self, name, student_id, personalised_notification, category=None, can_post=False):
        super().__init__(name)
        self.student_id = student_id
        self.chatroom = None
        # Attach the student to personalised_notification so it can be added to the subscriber list
        personalised_notification.attach(self)
        # Add categories - so student can subscribe to a list of categories for personalised notification
        self.category = [] if category is None else category
        #  set permission to post - Default False
        self.can_post = can_post
        # to make personalised dashboard
        self.dashboard = Dashboard(name)

    def create_chatroom(self, name):
        chat_room = chatroom.ChatRoom(name)
        print(f"{self.name} created a chatroom: {name}")
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

    # Add sub method - with references to example code from week5 BUS
    def sub(self, msg):
        print(f"[<<< User {self.name}] Notification Received: {msg}")
        self.dashboard.add_item(msg) # Add the message to dashboard

    # only certain students can post so defaulted to False but can set to True for student who can post (see example user in personalised_notification_menu.py)
    def canPostAnnouncement(self):
        return self.can_post

class Staff(User):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id

    # since all staff can post, it is set to True here
    def canPostAnnouncement(self):
        return True
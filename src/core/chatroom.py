class ChatRoom():
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def join_chatroom(self, user):
        if user not in self.users:
            self.users.append(user)

    def get_room_students(self):
        for user in self.users:
            print(f"- {user.name}")

    def is_user_in_chatroom(self, user):
        return user in self.users

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.name} join the chatroom.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.name} left the chatroom.")


    def broadcast(self, sender, content):
        self.messages.append(f"{sender}：{content}")

from user import Student

if __name__ == "__main__":
    alice = Student("Alice", "1234567890")

    chatroom = alice.create_chatroom('gossip')

    bob = Student("Bob", "0987654321")
    bob.join_chatroom(chatroom)

    while True:
        for user in chatroom.users:
            message = input(f"{user.name}：")
            if message.lower() in ['exit']:
                user.leave_chatroom()

            # TODO: AI
            if user == "AI":
                print(f"{user}：auto reply\n")
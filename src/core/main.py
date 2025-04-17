from User import Student
from brummie import BrummieAssistant

if __name__ == "__main__":
    alice = Student("Alice", "1234567890")
    brummie = BrummieAssistant()
    chatroom = alice.create_chatroom('gossip')

    bob = Student("Bob", "0987654321")
    bob.join_chatroom(chatroom)
    chatroom.add_user(brummie)

    while True:
        for user in [alice, bob]:
            message = input(f"{user.name}：")
            if message.lower() in ['exit']:
                user.leave_chatroom()
                break
            chatroom.broadcast(user, message)

            if "@brummie" in message.lower():
                clean = message.lower().replace("@brummie", "").strip()
                response = brummie.respond_to_query(clean, user)
                print(response)

            # Brummie respond only if the message contains @brummie





from User import Student
from brummie import BrummieAssistant
from personalised_notification_menu import personalised_notification
from notification import PersonalisedNotification

if __name__ == "__main__":
    # call menu from personalised_notification_menu.py
    # personalised_notification()
    # need to integrate menu with chatroom
    # updated example user Alice and Bob because an extra attribute was added to Student class
    notification_system = PersonalisedNotification()

    alice = Student("Alice", "1234567890", notification_system)
    brummie = BrummieAssistant()
    chatroom = alice.create_chatroom('gossip')

    bob = Student("Bob", "0987654321", notification_system)
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
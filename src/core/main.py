from user import Student
from brummie import BrummieAssistant
from personalised_notification_menu import personalised_notification
from notification import PersonalisedNotification

def handle_chatroom():
    notification_system = PersonalisedNotification()
    alice = Student("Alice", "1234567890", notification_system)
    brummie = BrummieAssistant()
    chatroom = alice.create_chatroom('BUS')

    bob = Student("Bob", "0987654321", notification_system)
    bob.join_chatroom(chatroom)
    chatroom.add_user(brummie)
    
    while True:
        for user in [alice, bob]:
            message = input(f"{user.name}：")
            if message.lower() in ['exit']:
                user.leave_chatroom()
                return
            chatroom.broadcast(user, message)

            if "@brummie" in message.lower():
                clean = message.lower().replace("@brummie", "").strip()
                response = brummie.respond_to_query(clean, user)
                print(response)

def main():
    while True:
        try:
            choice = int(input("\nMenu:\n"
                               "1. Chat room\n"
                               "2. Personalised notification\n"
                               "3. Exit\n"
                               "Please select the feature you would like to experience: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-3.")
            continue

        match choice:
            case 1:
                handle_chatroom()
            case 2:
                personalised_notification()
            case 3:
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
                
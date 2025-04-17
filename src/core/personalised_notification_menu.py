from User import Staff, Student
from notification import PersonalisedNotification, Announcement

def personalised_notification():
    # Create notification_system object
    notification_system = PersonalisedNotification()

    # hardcode - example users
    users = {
        "1111": Staff("Amy", "1111"),
        "2111": Student("Kat", "2111", notification_system,["Exams", "Events"]),
        "3111": Student("Tom", "3111", notification_system,["Events", "Sports"], can_post=True)
    }

    # example announcements -start
    # - uncomment to use if don't want to type in announcement to see if it's working everytime

    # announcements = [
    #     Announcement("Exam", "DSAD exam next week!", "Exams"),
    #     Announcement("Event", "Social event this Saturday.", "Events"),
    #     Announcement("Sports Day", "Sports Day next month.", "Sports")
    # ]
    # staff = users["1111"]
    # for announcement in announcements:
    #     notification_system.postAnnouncement(announcement, staff)

    # example announcements - end

    current_user = None

    # Add menu like in Software Workshop 1
    while True:
        if not current_user:
            user_id = input("Please enter your ID: ")
            current_user = users.get(user_id, None)
            if current_user:
                print(f'Welcome {current_user.name}')
            else:
                print("Invalid ID. Please try again.")
                continue

        try:
            choice = int(input("\nMenu:\n"
                               "1. Post Announcement\n"
                               "2. Set Preferences\n"
                               "3. View Dashboard\n"
                               "4. Logout\n"
                               "5. Exit\n"
                               "Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-5.")
            continue

        match choice:
            case 1: # let authorised to input announcement
                if current_user.canPostAnnouncement():
                    title = input("Enter announcement title: ")
                    content = input("Enter announcement content: ")
                    category = input("Enter category (e.g., Exams, Events, Sports, Workshops): ")
                    announcement = Announcement(title, content, category)
                    notification_system.postAnnouncement(announcement, current_user)
                else:
                    print(f"[User {current_user.name}] Not authorised to post announcements.")

            case 2:
                if isinstance(current_user, Student):  # check it is a student as only student can set their preferred categories for now
                    # This let students add the category they want to subscribe to
                    category = input("Enter a category to subscribe to (e.g., Exams, Events, Sports, Workshops): ")
                    if category not in current_user.category:
                        current_user.category.append(category)
                        print(f"[{current_user.name}] Subscribed to category: {category}")
                    else:
                        print(f"[{current_user.name}] Already subscribed to category: {category}")
                else:
                    print("Subscription options are not available for staff yet.")

            case 3:
                if isinstance(current_user, Student):
                    dashboard_items = notification_system.generateDashboard(current_user)
                    if dashboard_items:
                        print(dashboard_items)
                    else:
                        print("Dashboard is empty.")
                else:
                    print("Dashboard is not available for staff yet.")

            case 4:
                current_user = None
                print("Logged out successfully.")

            case 5:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice entered. You must enter a number from 1-5.")
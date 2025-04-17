# Add classes needed for personalised notification feature - with references to class diagram
class Announcement:
    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category

class Notification:
    def __init__(self, user, message):
        self.user = user
        self.message = message

class Dashboard:
    def __init__(self, user):
        self.username = user
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def view_items(self):
        return self.items

# Act as broker in publish/subscriber pattern - like a middleman between publisher and subscriber
# in our case - publishers are authorised users and subscribers are students
class PersonalisedNotification(object):
    def __init__(self):
        self._subscribers = [] # Subscribers list

    # add user to subscriber list
    def attach(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    # remove user from subscriber
    def detach(self, subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    # class methods - with references to class diagram
    def postAnnouncement(self, announcement, user):
        if user.canPostAnnouncement(): # this stop authorised user from posting announcement
            print(f"***Announcement Posted*** Title: {announcement.title}, Category: {announcement.category}, Content: {announcement.content}")
            # if authorised, the announcement is posted, then
            # it goes through the subscribers in the subscribers list to check
            # if the announcement category matches the category for the subscriber
            # if so, it will generate a notification message and use the sendNotification method below to send
            for subscriber in self._subscribers:
                if announcement.category in subscriber.category:
                    notification_message = f"Announcement: {announcement.title} - {announcement.content}"
                    self.sendNotification(subscriber, notification_message)
        else:
            print(f"Not authorised to post announcement.")

    # class methods - with references to class diagram
    # method to send notification
    def sendNotification(self, user, message):
        print(f"[>>> Notification Sent to {user.name}] Message: {message}")
        notification = Notification(user.student_id, message)
        user.sub(notification.message) # .sub method from Student class
        return notification

    # class methods - with references to class diagram
    # it returns the list of items from the dashboard
    def generateDashboard(self, user):
        print(f"\n[---Dashboard for {user.name}---]")
        return user.dashboard.view_items()
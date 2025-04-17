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
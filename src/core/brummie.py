class BrummieAssistant:
    def __init__(self, user):
        self.user = user
        self.name = "Brummie"

    def respond_to_query(self, query):
        if "assignment" in query:
            return f"{self.name}: Hi {self.user.name}, Your next assignment is due on May 8th."
        elif "study plan" in query:
            if 'orchestra' in self.user.preference:
                return f"{self.name}: Hi {self.user.name}, Based on your recommendations of interest, you can attend the orchestra concert from 1:30-3:30, then review for next Friday's exam in the library from 4:00-5:00!"
            else:
                return f"{self.name}: Hi {self.user.name}, you can review for next Friday's exam in the library from 1:30-5:00!"
        elif "counselor" in query or "appointment" in query:
            return "You can book a mental health counseling session at: www.birmingham.ac.uk.mentalhealth/booking"
        elif "transport" in query:
            return f"{self.name}: Hi {self.user.name}, You can take bus 63 at the north road stop and it will arrive in 10 minutes."
        else:
            return f"{self.name}: Sorry {self.user.name}, , I didn’t understand that. Try asking about assignments, study plans, or transport."

class StudyRoom:
    def __init__(self):
        self.members = []
        self.messages = []

    def send_message(self, sender, message):
        self.messages.append((sender.name, message))
        print(f"{sender.name}: {message}")

        #Brummie respond only if the message contains @brummie
        if "@brummie" in message.lower():
            for member in self.members:
                if isinstance(member, BrummieAssistant):
                    cleaned_message = message.lower().replace("@brummie", "").strip()
                    response = member.respond_to_query(cleaned_message)
                    if response:
                        self.send_message(member, response)

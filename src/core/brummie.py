from user import User

#brummie is an AI assistant in our study room
class BrummieAssistant(User):
    def __init__(self):
        super().__init__("Brummie")
        self.name = "Brummie"

    def respond_to_query(self, query,sender):
        if "assignment" in query:
            return f"{self.name}: Hi {sender.name}, Your next assignment is due on May 8th."
        elif "study plan" in query:
            return f"{self.name}: Hi {sender.name}, Based on your recommendations of interest, you can attend the orchestra concert from 1:30-3:30, then review for next Friday's exam in the library from 4:00-5:00!"
        elif "counselor" in query or "appointment" in query:
            return "You can book a mental health counseling session at: www.birmingham.ac.uk.mentalhealth/booking"
        elif "transport" in query:
            return f"{self.name}: Hi {sender.name}, You can take bus 63 at the north road stop and it will arrive in 10 minutes."
        else:
            return f"{self.name}: Sorry {sender.name},  I didn’t understand that. Try asking about assignments, study plans, or transport."


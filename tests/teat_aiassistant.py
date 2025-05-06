import pytest
from user import Student
from brummie import BrummieAssistant
from notification import PersonalisedNotification

@pytest.fixture
def brummie():
    return BrummieAssistant()

@pytest.fixture
def sender():
    notification_system = PersonalisedNotification()
    alice = Student("Alice", "1234567890", notification_system)
    return alice

#Positive test:assignment, study plan, counselor, transport
def test_aiassistant_positive(brummie,sender):
    # assignment
    response = brummie.respond_to_query("Tell me about the assignment", sender)
    assert "assignment is due" in response

    # study plan
    response = brummie.respond_to_query("Give me a study plan", sender)
    assert "study plan" in response or "library" in response

    # counselor
    response = brummie.respond_to_query("How do I book a counselor?", sender)
    assert "mental health" in response

    # transport
    response = brummie.respond_to_query("How do I take transport to campus?", sender)
    assert "bus 63" in response

# Negative test: Input is semantically irrelevant, Brummie should gracefully fallback
def test_aiassistant_negative(brummie,sender):
    response = brummie.respond_to_query("Do you like tofu?", sender)
    assert "didn’t understand" in response
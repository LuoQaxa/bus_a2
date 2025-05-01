import pytest
from chatroom import ChatRoom
from user import Student, Staff
from notification import PersonalisedNotification, Announcement

# Positive test case
def test_notification_positive(capsys):
    # Create users
    notification_system = PersonalisedNotification()
    staff = Staff("Ellie", "1001")
    student = Student("Ben", "2001", notification_system, ["Exams"])

    # Create and post announcements
    announcement = Announcement("Exam", "CS exam on 13th May", "Exams")
    notification_system.postAnnouncement(announcement, staff)

    # Capture the printed output in console
    captured = capsys.readouterr()

    # Check that announcements are posted and notification are sent to the relevant student.
    assert "***Announcement Posted*** Title: Exam, Category: Exams, Content: CS exam on 13th May" in captured.out
    assert f"[>>> Notification Sent to {student.name}] Message: Announcement: Exam - CS exam on 13th May" in captured.out
    assert f"[<<< User {student.name}] Notification Received: Announcement: Exam - CS exam on 13th May" in captured.out

# Negative test case
def test_notification_negative(capsys):
    # Create users
    notification_system = PersonalisedNotification()
    staff = Staff("Ellie", "1001")
    student = Student("Ben", "2001", notification_system, ["Exams"])

    # Create and post announcements
    announcement = Announcement("Event", "Equality, Diversity and Inclusion Celebration on 7th May", "Events")
    notification_system.postAnnouncement(announcement, staff)

    # Capture the printed output in console
    captured = capsys.readouterr()

    # Check that announcements are posted and notification are not sent to student who is not subscribed to the relevant category.
    assert "***Announcement Posted*** Title: Event, Category: Events, Content: Equality, Diversity and Inclusion Celebration on 7th May" in captured.out
    assert f"[>>> Notification Sent to {student.name}] Message: Announcement: Event - Equality, Diversity and Inclusion Celebration on 7th May" not in captured.out
    assert f"[<<< User {student.name}] Notification Received: Announcement: Event - Equality, Diversity and Inclusion Celebration on 7th May" not in captured.out
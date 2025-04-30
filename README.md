# UniSupport – A Comprehensive University Support System

UniSupport is an online learning platform created to support students throughout their virtual education journey. This prototype highlights three main features designed to make student life more manageable and engaging.

### personalized Notification

Different roles and permissions can be set in this module, enhancing the authorization management and allowing for easier maintenance and updates. In addition, selecting the notification categories makes it easier for students to focus on the information that interests them the most.

### Chat Room

This feature integrates the AI helper (Brummie) into conversations, allowing students to easily discuss schoolwork online. With Brummie's involvement, not only on schoolwork but also campus life information for students anytime and anywhere, striking a balance between schoolwork and campus life.

### Brummie (AI Assistant)

On academy-wise, the AI assistant Brummie integrates personalized information for assignments such as deadlines, school activity recommendations, and transportation. Furthermore, it detects texts and guides them to meet professionals on campus if needed.

---

### Languages, Object-Oriented Design, Design Patterns, Testing Framework

- This prototype uses Python as the primary programming language.
- It showcases the inheritance relationships in User module, association relationships in personalizedNotification (e.g., subscriber() has User), and Chatroom (e.g., join_chatroom() has User) module.
- Publish/Subscriber is the design pattern implemented in this prototype. For example, In the Notification.py, the PersonalisedNotification class is a mediator between subscribers (students) and publishers (authorized users). It automatically sends notifications to relevant students when new announcements are published.
- For test case implementation, we chose pytest as our testing framework, as it is famous for fastly building functional testing for applications.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.10 or above
- `pip` (Python package manager)

---

## Installation

1. Clone the repository in terminal:

   ```bash
   git clone https://github.com/LuoQaxa/bus_a2.git
   cd bus_a2
   ```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Navigate to the `src/core` directory

```bash
cd src/core
```

2. Run the main program:

```bash
python main.py
```

### Usage Guide

When you run the program, you will see the following menu in terminal:

```bash
Menu:
1. Chat room
2. Personalised notification
3. Exit
Please select the feature you would like to experience:
```

- **Option 1: Chat Room**
  Enter the chat room to interact with other users and the AI assistant, Brummie.

  You will see the user who created the chat room and the other users who are in the chat room at the same time.

  You can:

  - Type messages to communicate.
  - Mention AI assistant by `@brummie` in your message to ask Brummie a question.
  - Type `exit` in the message and send it out to leave the chat room.

* **Option 2: Personalised Notification**
  Manage your notification preferences and view announcements.

  - Log in with your user ID. (For testing, you can try ID `1111` for staff, `2111` and `3111` for student)
  - Post announcements (if authorised).
  - Subscribe to categories you are interested in.
  - View your personalised dashboarb.

* **Option 3: Exit**
  Exit the program.

### Testing

To run the test suite, use the following command:

```bash
pytest
```

This will execute all test cases located in the `tests/` directory.

### Contribution Breakdown

- **Qian Luo**(20%): Implemented the Chat Room module and integrated the AI assistant Brummie.
- **Stephanie Fung**(20%): Developed the Personalised Notification system.
- **Wangyue Ma**(20%): Developed the function of the AI assistant Brummie.
- **Wei-Xuan Li**(20%): Designed the system architecture, demonstrated the prototype in demo video.
- **Ailin Yu**(20%): Wrote the step-by-step instructions in README file, explained development methodology and testing framework in video.

**[Wrote test cases - need to discuss]**

# bus_a2

Git Collaboration Workflow

1. Feature Development

```bash
# Create and switch to a new feature branch from main

git checkout -b feat/xxx  # Branch naming convention: feat<feature-name>

# Push the branch to remote repository

git push -u origin feat/xxx
```

2. Creating Pull Request
   Go to your repository on GitHub/GitLab

create "New Pull Request"

3. Resolving Conflicts (if any)

```bash
# While on your feature branch
git pull origin main   # Merge latest main branch changes
# Resolve conflicts manually in affected files
git add .
git commit -m "resolve: merge conflicts with main"
git push origin feat/xxx
```

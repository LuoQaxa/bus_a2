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


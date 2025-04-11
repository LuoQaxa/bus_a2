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

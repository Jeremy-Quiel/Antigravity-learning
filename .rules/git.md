# Version Control and Git Rules

## 1. Purpose
Ensure continuous persistence, synchronization, and traceable versioning of all codebase modifications with the remote GitHub repository.

## 2. Scope
Applies to all autonomous agents, developers, and automated tools creating, modifying, or deleting files in this workspace.

## 3. Mandatory Rules
- **Immediate Commit:** Whenever a file change is made, an immediate commit must be created with a clear, descriptive message adhering to *Conventional Commits*.
- **Remote Synchronization (Push):** All commits must be pushed (`git push`) to their corresponding remote branch on GitHub.
- **Atomicity:** Changes must be committed in coherent, logical, and self-contained units without accumulating untracked or uncommitted changes.

## 4. Branch Creation Rules
- **Mandatory Origin:** All new branches must be created exclusively from the `main` branch.
- **Prior Synchronization:** Before creating any new branch, verify that the local `main` branch is fully synchronized with the remote (`git pull origin main`).
- **Clean Working Tree:** Ensure there are no unstaged or uncommitted local changes prior to branching out.

```bash
# 1. Switch to main and pull latest remote changes
git checkout main
git pull origin main

# 2. Verify clean status
git status

# 3. Create and switch to the new feature/task branch
git checkout -b <type>/<descriptive-name>
```

## 5. Standard Execution Workflow
```bash
# 1. Stage modified files
git add .

# 2. Commit with descriptive message
git commit -m "type: concise description of change"

# 3. Synchronize with remote branch
git push origin <current_branch>
```
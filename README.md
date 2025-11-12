# 📝 my_cli_todolist

A lightweight command-line todo list manager for organizing and tracking your tasks efficiently.

---

## 📦 Installation

1. Navigate to the project directory:
```bash
cd my_todo_list
```

2. (Optional) Uninstall any previous version:
```bash
pipx uninstall todo
```

3. Install the package:
```bash
pipx install .
```

---

## 🚀 Usage

### ➕ Adding a new task
```bash
todolist add "Buy groceries"
```
**Output:** `Task added successfully (ID: 1)`

### ✏️ Updating a task
```bash
todolist update 1 "Buy groceries and cook dinner"
```

### 🗑️ Deleting a task
```bash
todolist delete 1
```

### 🔄 Marking task status
Mark a task as in progress:
```bash
todolist mark-in-progress 1
```

Mark a task as done:
```bash
todolist mark-done 1
```

### 📋 Listing tasks

List all tasks:
```bash
todolist list
```

Filter tasks by status:
```bash
todolist list done           # Show completed tasks
todolist list todo           # Show pending tasks
todolist list in-progress    # Show in-progress tasks
```

---

## 📄 License

Created by Davide Ariotto
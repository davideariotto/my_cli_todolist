# my_cli_todolist
Simple CLI todolist tool 

## To install
cd my_todo_list
pipx uninstall todo (OPTIONAL)
pipx install .

## How to use it:

### Adding a new task
todolist add "Buy groceries"

-- Output: Task added successfully (ID: 1)

### Updating and deleting tasks
todolist update 1 "Buy groceries and cook dinner"
todolist delete 1

### Marking a task as in progress or done
todolist mark-in-progress 1
todolist mark-done 

### Listing all tasks
todolist list

### Listing tasks by status
todolist list done
todolist list todo
todolist list in-progress
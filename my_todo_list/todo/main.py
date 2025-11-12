import sys
import json
import os

from todo.todo_list import TodoList

# Calculate absolute path of "storage" folder inside the cloned repo
PROJECT_ROOT = os.path.abspath(os.getcwd())
FILENAME = os.path.join(PROJECT_ROOT, "data.json")

def ensure_storage():
    """
    Create file if not exist.
    """
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump([], f)

def load_todo_list():
    """
    Load JSON file if it exists, otherwise return an empty list.
    """
    ensure_storage()
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_todo_list(data):
    """
    Write data to JSON file.
    """
    ensure_storage()
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def main():
    if len(sys.argv) < 2:
        print("ERROR: No command given. \nUse one of: add, update, delete, mark-in-progress, mark-done, list")
        sys.exit(1)
    
    t = TodoList(load_todo_list())
    command = sys.argv[1]
    
    if command == "add":
        t.create_task(sys.argv[2])
    elif command == "update":
        t.update_task(sys.argv[2], sys.argv[3])
    elif command == "delete":
        t.delete_task(sys.argv[2])
    elif command == "mark-in-progress":
        t.mark_in_progress(sys.argv[2])
    elif command == "mark-done":
        t.mark_done(sys.argv[2])
    elif command == "list":
        filter = sys.argv[2] if len(sys.argv) > 2 else None
        if filter:
            t.list_filtered_tasks(filter)
        else:
            t.list_tasks()
    else:
        print(f"ERROR: command {command} doesn't exist. \nUse one of: add, update, delete, mark-in-progress, mark-done, list")

    save_todo_list(t.to_json_list())

    return


if __name__ == "__main__":
    main()
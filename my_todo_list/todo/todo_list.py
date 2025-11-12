from todo.task import Task

class TodoList():
    def __init__(self, json_list):
        self.list = TodoList.from_list(json_list) # Build a dict of tasks from JSON
        self.length = len(self.list)  # Tasks count
    
    def get_list(self):
        return self.list
    
    def get_length(self):
        return self.length
    
    def increment_length(self):
        self.length += 1
    
    @staticmethod
    def from_list(json_list):
        """
        Convert JSON list of task dicts into a dict of Task objects.
        Keys = task IDs
        Values = Task objects
        """
        tasks = {}

        for json_task in json_list:
            task = TodoList.from_dict(json_task)
            tasks[task.id] = task  # use ID as key

        return tasks
    
    def to_json_list(self):
        """
        Convert internal dict of Task objects into a JSON-serializable list.
        """
        return [task.to_dict() for task in self.list.values()]
    
    @staticmethod
    def from_dict(d):
        """
        Convert a dict into a Task object.
        """
        return Task(d.get("id"), d.get("name"), d.get("state"))
    
    def create_task(self, name):
        """
        Create new task.
        """
        self.increment_length()
        task = Task(str(self.length), name)
        self.list[str(self.length)] = task
        print(f"Task created successfully!! ID = {self.length}")
    
    def update_task(self, id, name):
        """ 
        Update task name.
        """
        self.list[id].set_name(name)
        print(f"Task {id}: name updated")
    
    def delete_task(self, id):
        """
        Delete task.
        """
        del self.list[id]
    
    def mark_in_progress(self, id):
        """
        Mark task as in-progress.
        """
        self.list[id].set_state("in-progress")
        print(f"Task {id} in-progress")
    
    def mark_done(self, id):
        """
        Mark task as done.
        """
        self.list[id].set_state("done")
        print(f"Task {id} done")
    
    def list_tasks(self):
        """
        List all current tasks.
        """
        print("TODO LIST:")
        for task in self.list.values():
            print(task)
    
    def list_filtered_tasks(self, filter):
        """
        List tasks filtered by state.
        """
        print(f"TODO LIST: {filter}")
        for task in [t for t in self.list.values() if t.get_state() == filter]:
            print(task)
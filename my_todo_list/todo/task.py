class Task():
    def __init__(self, id, name, state="todo"):
        self.id = id
        self.name = name
        self.state = state

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def set_name(self, name):
        self.name = name

    def set_state(self, state):
        self.state = state

    def to_dict(self):
        return {"id": self.id, "name": self.name, "state": self.state}
    
    def __str__(self):
        return f"Task {self.id}: {self.name} [{self.state}]"
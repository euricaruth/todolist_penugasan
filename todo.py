import os
import json

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description, deadline):
        task = {
            "description": description,
            "deadline": deadline,
            "completed": False
        }
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            return True
        return False

    def edit_task(self, index, new_description, new_deadline):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["description"] = new_description
            self.tasks[index]["deadline"] = new_deadline
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

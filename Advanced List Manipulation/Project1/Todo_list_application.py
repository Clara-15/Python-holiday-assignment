# todo_app.py
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_completed(self, task_index):
        self.tasks[task_index] += " (Completed)"

    def display_list(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    def delete_task(self, task_index):
        del self.tasks[task_index]

# Usage example
todo_list = TodoList()
todo_list.add_task("Task 1")
todo_list.add_task("Task 2")
todo_list.display_list()
todo_list.mark_completed(0)
todo_list.display_list()
todo_list.delete_task(1)
todo_list.display_list()

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority="Normal"):
        self.tasks[task] = priority
        print(f"Task '{task}' added with priority '{priority}'.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def update_priority(self, task, new_priority):
        if task in self.tasks:
            self.tasks[task] = new_priority
            print(f"Priority of task '{task}' updated to '{new_priority}'.")
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Current tasks:")
            for task, priority in self.tasks.items():
                print(f"- {task} (Priority: {priority})")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Priority")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            priority = input("Enter the priority (default is 'Normal'): ")
            todo_list.add_task(task, priority)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter the task to update: ")
            new_priority = input("Enter the new priority: ")
            todo_list.update_priority(task, new_priority)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

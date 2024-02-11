class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Task completed successfully!")
        else:
            print("Invalid task index!")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. [{task['completed'] and 'X' or ' '}] {task['task']}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. Remove a task")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            task_manager.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to complete: ")) - 1
            task_manager.complete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to remove: ")) - 1
            task_manager.remove_task(index)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()

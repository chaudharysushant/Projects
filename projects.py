tasks = []

while True:
    print("\nMENU OPTIONS:\n"
          "1. Add Task\n"
          "2. View Tasks\n"
          "3. Update Task\n"
          "4. Delete Task\n"
          "5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Add Your Task: ")
        tasks.append(task)
        print("Task Added!\n")

    elif choice == "2":
        if not tasks:
            print("No tasks to show.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Enter the task number to update: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter the new task description: ")
                    tasks[task_num - 1] = new_task
                    print("Task updated!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    print(f"Task '{deleted_task}' deleted!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

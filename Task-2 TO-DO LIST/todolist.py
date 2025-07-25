tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks to show.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '3':
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")

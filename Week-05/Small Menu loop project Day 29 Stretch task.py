# Stretch task
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found.")
    elif choice == "3":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\nYour task:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please choose 1, 2, 3, or 4.")

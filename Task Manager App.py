menu = ["Add New Task", "View All Tasks", "Delete Task", "Exit"]
tasks = []

def add_task():
    chore = input("Enter the task description: ")
    due_date = input("Enter the due date: ")
    task = {"chore": chore, "due_date": due_date}
    tasks.append(task)
    print(f"Task '{chore}' with due date '{due_date}' added successfully!")
    with open("tasks.txt", "a") as file:
        file.write(f"Task: {chore}, Due Date: {due_date}\n")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"Task {i}: {task['chore']} - Due Date: {task['due_date']}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                deleted_task = tasks.pop(task_number)
                print(f"Task '{deleted_task['chore']}' with due date '{deleted_task['due_date']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        

def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"Task: {task['chore']}, Due Date: {task['due_date']}\n")


# Main loop
while True:
    print("\nMenu:")
    for i, option in enumerate(menu, start=1):
        print(f"{i}. {option}")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
            save_tasks_to_file()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

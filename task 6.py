import json
tasks = []
def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# 1. Add Task
def add_task(description):
    task_id = len(tasks) + 1
    task = {"id": task_id, "description": description, "status": "pending"}
    tasks.append(task)
    save_tasks()
    print(f"Task '{description}' added with ID {task_id}.")

# 2. View Tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")

# 3. Remove Task
def remove_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks()
    print(f"Task with ID {task_id} removed.")

# 4. Mark Task as Completed
def mark_task_completed(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'completed'
            save_tasks()
            print(f"Task with ID {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

# 5. Edit Task
def edit_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            save_tasks()
            print(f"Task with ID {task_id} updated.")
            return
    print(f"Task with ID {task_id} not found.")

# 6. Search Task
def search_task(keyword):
    found_tasks = [task for task in tasks if keyword.lower() in task['description'].lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
    else:
        print(f"No tasks found containing '{keyword}'.")

# 7. Filter Tasks by Status
def filter_tasks_by_status(status):
    filtered_tasks = [task for task in tasks if task['status'] == status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
    else:
        print(f"No {status} tasks found.")

# 8. Clear All Tasks
def clear_all_tasks():
    confirmation = input("Are you sure you want to clear all tasks? (y/n): ")
    if confirmation.lower() == 'y':
        tasks.clear()
        save_tasks()
        print("All tasks cleared.")
    else:
        print("Clear all tasks canceled.")

# 9. Sort Tasks
def sort_tasks(by="id"):
    if by == "id":
        sorted_tasks = sorted(tasks, key=lambda x: x['id'])
    elif by == "status":
        sorted_tasks = sorted(tasks, key=lambda x: x['status'])
    else:
        print("Invalid sort option.")
        return
    for task in sorted_tasks:
        print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")

def menu():
    load_tasks()  
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks (Pending/Completed)")
        print("8. Clear All Tasks")
        print("9. Sort Tasks (by ID or Status)")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to edit: "))
            new_description = input("Enter new task description: ")
            edit_task(task_id, new_description)
        elif choice == '6':
            keyword = input("Enter keyword to search tasks: ")
            search_task(keyword)
        elif choice == '7':
            status = input("Enter status to filter by (pending/completed): ")
            filter_tasks_by_status(status)
        elif choice == '8':
            clear_all_tasks()
        elif choice == '9':
            sort_by = input("Sort by (id/status): ")
            sort_tasks(sort_by)
        elif choice == '0':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()

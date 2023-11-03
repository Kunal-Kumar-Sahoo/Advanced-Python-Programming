import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Initialize tasks data structure
tasks = []

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description, due_date, status):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status
    }
    tasks.append(task)
    save_tasks()

def search_task_by_title(title):
    for task in tasks:
        if task["title"] == title:
            return task
    return None

def update_task_status(title, new_status):
    task = search_task_by_title(title)
    if task:
        task["status"] = new_status
        save_tasks()

def delete_task(title):
    task = search_task_by_title(title)
    if task:
        tasks.remove(task)
        save_tasks()

def display_tasks():
    for task in tasks:
        print(f"Title: {task['title']}\nStatus: {task['status']}\n")

def main():
    tasks.extend(load_tasks())

    while True:
        print("Task Tracking Application")
        print("1. Add Task")
        print("2. Search Task")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Display All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            status = input("Enter status (pending, completed, in progress): ")
            add_task(title, description, due_date, status)

        elif choice == "2":
            title = input("Enter task title to search: ")
            task = search_task_by_title(title)
            if task:
                print("Task Found:")
                print(f"Title: {task['title']}")
                print(f"Description: {task['description']}")
                print(f"Due Date: {task['due_date']}")
                print(f"Status: {task['status']}")
            else:
                print("Task not found.")

        elif choice == "3":
            title = input("Enter task title to update: ")
            new_status = input("Enter new status: ")
            update_task_status(title, new_status)

        elif choice == "4":
            title = input("Enter task title to delete: ")
            delete_task(title)

        elif choice == "5":
            display_tasks()

        elif choice == "6":
            save_tasks()
            print("Exiting the application.")
            break

if __name__ == "__main__":
    main()
from db import operations
# handles task logic (add/update/delete/show)

def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")
    operations.add_task(title, description)

def delete_task():
    title = input("Enter the title of the task to delete: ").strip()
    if not title:
        print(" Title cannot be empty.")
        return
    else:
        operations.delete_task(title)

def update_task():
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        title = input("Enter the title of the task to update: ").strip()
        new_title = input("Enter the new title (leave blank to keep the same): ")
        new_description = input("Enter the new description (leave blank to keep the same): ")

        if not title and not new_title and not new_description:
            print("Title and new title cannot be empty.")
            return
        else:
            operations.update_task(task_id, title, new_title, new_description)

    except Exception as e:
        print(f"An error occurred: {e}")

def show_all_task():
    operations.show_tasks()


def manu():
    try:
        while True:
            print("------ Menu ------")
            print("1. Add task")
            print("2. Delete task")
            print("3. Update task")
            print("4. Show all tasks")
            print("5. Exit")
            choice = input("Enter your choice: ").lower()
            if choice == "1":
                add_task()
            elif choice == "2":
                delete_task()
            elif choice == "3":
                update_task()
            elif choice == "4":
                show_all_task()
            elif choice == "5":
                print("Thank you for using our application!")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
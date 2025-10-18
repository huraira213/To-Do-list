from .connection import get_connection

def add_task(title, description):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (task_title, task_description) VALUES (%s, %s)",
            (title, description)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Task added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def show_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    for r in rows:
        #print(f"Task ID: {r[0]}, Task Title: {r[1]}, Task Description: {r[2]}")
        print("------")
        print(f"{r[0]}. {r[1]}")
        print(r[2])
        print("------")

def delete_task(title):
        """Delete a task by title."""
        try:
            conn = get_connection()
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM tasks WHERE task_title = %s", (title,))
                    if cursor.rowcount == 0:
                        print(" No task found with that title.")
                    else:
                        print("Task deleted successfully!")
        except Exception as e:
            print(f"Error deleting task: {e}")

def update_task(task_id, title, new_title, new_description):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if the task exists
        cursor.execute("SELECT * FROM tasks WHERE task_id = %s AND task_title = %s", (task_id, title))
        task = cursor.fetchone()

        if not task:
            print("No matching task found.")
            return

        # Use old values if new ones are empty
        if not new_title:
            new_title = task[1]   # existing title
        if not new_description:
            new_description = task[2]   # existing description

        # Update both fields at once
        cursor.execute(
            "UPDATE tasks SET task_title = %s, task_description = %s WHERE task_id = %s",
            (new_title, new_description, task_id)
        )

        conn.commit()
        print("Task updated successfully!")

    except Exception as e:
        print(f"Error updating task: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

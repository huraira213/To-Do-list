import psycopg2
# handles PostgreSQL connection setup


def get_connection():
    """Establish and return a PostgreSQL connection."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="todolist_db",
            user="postgres",
            password="ali 33",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def create_table():
    """Create the tasks table if it does not exist."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Execute a command: create datacamp_courses table
        cur.execute("""CREATE TABLE IF NOT EXISTS tasks
                       (
                           task_id         SERIAL PRIMARY KEY,
                           task_title       VARCHAR(50) UNIQUE NOT NULL,
                           task_description VARCHAR(100)       NOT NULL
                       );
                    """)

        conn.commit()
        cur.close()
        conn.close()
        print("Table 'tasks' created (if it didn’t exist).")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")

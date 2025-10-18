from db.connection import create_table
from models.task_manager import manu

# main entry point (runs the app)

def main():
    create_table()
    manu()

if __name__ == "__main__":
    main()
import sqlite3
from sqlite3 import Error

class DatabaseConnection:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = None
        self.db_file = db_file

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connection to database {self.db_file} successful.")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def get_connection(self):
        """Return the current database connection."""
        return self.connection
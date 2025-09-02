# filepath: /sql-chatbot-app/sql-chatbot-app/packages/server-python/src/services/retriever.py

import sqlite3  # or the appropriate database library
from src.db.connection import get_db_connection  # Assuming this function is defined to get a DB connection

class Retriever:
    def __init__(self):
        self.connection = get_db_connection()

    def retrieve_response(self, user_input):
        cursor = self.connection.cursor()
        query = "SELECT response FROM chatbot_responses WHERE user_input = ?"
        cursor.execute(query, (user_input,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return result[0]
        else:
            return "I'm sorry, I don't have an answer for that."
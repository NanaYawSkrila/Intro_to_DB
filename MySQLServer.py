# FILE: MySQLServer.py
# STEP 1: Create database alx_book_store using Python and MySQL

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (adjust user/password/host if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Skrila@1"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: confirmation close
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()

#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Skrila@1"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:   # Specific MySQL error handling
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure resources are closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()

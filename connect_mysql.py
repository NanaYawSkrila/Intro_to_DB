import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",             # change if you use another MySQL user
            password="Skrila@1" # replace with your MySQL password
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Server")

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("📚 Database 'alx_book_store' is ready.")

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 MySQL connection closed")

if __name__ == "__main__":
    connect_to_mysql()

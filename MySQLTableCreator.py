# FILE: MySQLTableCreator.py
# STEP 3: Create tables for alx_book_store database

import mysql.connector
from mysql.connector import Error

def create_tables():
    connection = None
    try:
        # Connect to MySQL server and use the alx_book_store database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Skrila@1",
            database="alx_book_store"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Authors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Authors (
                    author_id INT AUTO_INCREMENT PRIMARY KEY,
                    author_name VARCHAR(215) NOT NULL
                )
            """)

            # Books table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Books (
                    book_id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(130) NOT NULL,
                    author_id INT,
                    price DOUBLE,
                    publication_date DATE,
                    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
                )
            """)

            # Customers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                    customer_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_name VARCHAR(215) NOT NULL,
                    email VARCHAR(215) UNIQUE,
                    address TEXT
                )
            """)

            # Orders table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    order_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_id INT,
                    order_date DATE,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                )
            """)

            # Order_Details table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Order_Details (
                    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
                    order_id INT,
                    book_id INT,
                    quantity DOUBLE,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                    FOREIGN KEY (book_id) REFERENCES Books(book_id)
                )
            """)

            print("All tables created successfully in 'alx_book_store' database!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_tables()

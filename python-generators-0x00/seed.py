import csv
import mysql.connector
from mysql.connector import errorcode
import uuid


def connect_db():
    """Connect to MySQL server"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def create_database(connection):
    """Create ALX_prodev database if it doesn't exist"""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()


def connect_to_prodev():
    """Connect to ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # Replace with your MySQL password
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None


def create_table(connection):
    """Create user_data table"""
    cursor = connection.cursor()
    create_stmt = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(user_id)
    )
    """
    try:
        cursor.execute(create_stmt)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()


def insert_data(connection, csv_file):
    """Insert data from CSV if not already present"""
    cursor = connection.cursor()
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                user_id = row.get("user_id") or str(uuid.uuid4())
                name = row["name"]
                email = row["email"]
                age = float(row["age"])

                cursor.execute(
                    "SELECT * FROM user_data WHERE user_id = %s",
                    (user_id,)
                )
                exists = cursor.fetchone()

                if not exists:
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )

            except Exception as e:
                print(f"Skipping row due to error: {e}")
    connection.commit()
    cursor.close()

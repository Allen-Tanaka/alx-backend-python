import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the database"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # replace as needed
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch  # ✅ Using yield (not return)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """Prints users over age 25 using streaming batches"""
    for batch in stream_users_in_batches(batch_size):  # loop 1
        for user in batch:  # loop 2
            if user["age"] > 25:  # condition (not a loop)
                print(user)

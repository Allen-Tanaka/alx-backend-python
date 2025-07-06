import seed  # uses connect_to_prodev() from seed.py

def stream_user_ages():
    """Generator that yields user ages one by one from the database"""
    try:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for (age,) in cursor:  # ✅ One loop used here
            yield age

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def compute_average_age():
    """Computes average age using a memory-efficient generator"""
    total = 0
    count = 0

    for age in stream_user_ages():  # ✅ Second and final loop
        total += age
        count += 1

    average = total / count if count else 0
    print(f"Average age of users: {average:.2f}")

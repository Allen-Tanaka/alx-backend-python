import seed  # Assumes seed.py has connect_to_prodev()

def paginate_users(page_size, offset):
    """Helper to fetch a page of users from the database"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """Generator that lazily fetches paginated user data using yield"""
    offset = 0
    while True:  # ✅ Only one loop used
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

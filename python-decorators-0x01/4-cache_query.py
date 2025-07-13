import sqlite3
import functools

query_cache = {}

# DB connection handler
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Caching decorator
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Cache hit")
            return query_cache[query]
        else:
            print("Cache miss. Fetching from DB...")
            result = func(conn, query, *args, **kwargs)
            query_cache[query] = result
            return result
    return wrapper

# Function to fetch users with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call: runs query and caches
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call: uses cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)

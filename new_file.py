import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs

def get_user_input(prompt):
    return input(prompt)

def execute_query(query, params=None):
    # Placeholder connection details; replace these with your actual database credentials
    conn = psycopg2.connect(
        dbname='yourdbname', 
        user='yourdbuser', 
        password='yourdbpassword', 
        host='localhost'
    )
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        # Assuming it's a SELECT query, fetch the result
        data = cur.fetchall()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def main():
    username = get_user_input("Enter your username: ")
    # Use a parameterized query to safely include user input
    query = "SELECT * FROM users WHERE username = %s"
    params = (username,)
    user_data = execute_query(query, params)
    if user_data:
        for user in user_data:
            print(f"User data: {user}")
    else:
        print("No data found or an error occurred.")

if __name__ == "__main__":
    main()

import psycopg2

def get_user_input(prompt):
    return input(prompt)

def execute_query(query):
    conn = psycopg2.connect(
        dbname='yourdbname', 
        user='yourdbuser', 
        password='yourdbpassword', 
        host='localhost'
    )
    cur = conn.cursor()
    try:
        cur.execute(query)
        data = cur.fetchall()
        return data
    finally:
        cur.close()
        conn.close()

def main():
    username = get_user_input("Enter your username: ")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    user_data = execute_query(query)
    for user in user_data:
        print(f"User data: {user}")

if __name__ == "__main__":
    main()

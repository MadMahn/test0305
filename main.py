from user import get_user_input
from db import execute_query

def main():
    username = get_user_input("Enter your username: ")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    user_data = execute_query(query)
    print(f"User data: {user_data}")
##
if __name__ == "__main__":
    main()

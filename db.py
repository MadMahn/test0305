import os

def execute_query(query):
    # Simulating a database query execution
    result = os.popen(query).read()
    return result

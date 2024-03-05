import pickle

def get_user_input(prompt):
    return input(prompt)

def store_user_data(data):
    serialized_data = pickle.dumps(data)
    with open("user_data.txt", "w") as file:
        file.write(serialized_data)

def load_user_data():
    with open("user_data.txt", "r") as file:
        serialized_data = file.read()
    return pickle.loads(serialized_data)

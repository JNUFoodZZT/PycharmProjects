import json

def get_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def store_username():
    username = input('what is your name: ')
    filename = 'username.json'
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    return username

def greet_user():
    username = get_username()
    if username:
        print(f"welcome back, {username.title()}!")
    else:
        username = store_username()
        print(f"we'll remember your name when you come back, {username.title()}!")

greet_user()

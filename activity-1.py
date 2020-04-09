import json
import os

new_list = []

file_path = 'users.json'
def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

is_empty = is_file_empty(file_path)

if is_empty:
    print("file is empty")
else:
    with open('users.json', 'r') as file:
        old_users = json.load(file)

    for i in range(0, len(old_users)):
        new_list.append(old_users[i])
        
def print_all_users():
    for i in range(0, len(new_list)):
        print(f'Name: {new_list[i]["name"]}\nAge: {new_list[i]["age"]}')

run = True

while run == True:
    name = str(input("Enter your name: "))
    age = input("Enter your age: ")
    new_dict = {
        "name": name,
        "age": age
    }
    new_list.append(new_dict)
    for i in range(0, len(new_list)):
        print(f'Name: {new_list[i]["name"]}\nAge: {new_list[i]["age"]}')
    print("Add another user? (y/n)")
    user_input = input()
    if user_input == "n":
        break

print_all_users()

with open("users.json", "w") as users:
    json.dump(new_list, users, indent=4)








# [{
# 		"name": "johndoe",
# 		"age": 34
# 	},
# 	{
# 		"name": "marydoe",
# 		"age": 29
# 	}
# ]

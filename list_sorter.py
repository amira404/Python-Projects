# list_sorter.py

def get_user_list():
    user_list = []
    for index in range(5):
        num = int(input(f"Enter num {index+1}: "))
        user_list.append(num)
    return user_list

def sort_list(user_list):
    ascending_list = sorted(user_list)
    descending_list = sorted(user_list, reverse=True)
    return ascending_list, descending_list

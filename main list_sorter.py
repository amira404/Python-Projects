# Main.py

from list_sorter import get_user_list, sort_list

user_list = get_user_list()
print("The original list:", user_list)

ascending_list, descending_list = sort_list(user_list)
print('Ascending list:', ascending_list)
print('Descending list:', descending_list)

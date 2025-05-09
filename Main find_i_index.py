# Main.py

from find_i_index import find_i_positions

user_input = input("Enter your string: ")
positions = find_i_positions(user_input)

for pos in positions:
    print('i or I is in', pos)
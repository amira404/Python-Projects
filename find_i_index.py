# find_i_index.py

def find_i_positions(user_input):
    positions = []
    for index in range(len(user_input)):
        if user_input[index] == 'i' or user_input[index] == 'I':
            positions.append(index)
    return positions
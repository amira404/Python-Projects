
"""**Amira Muhammad**

**module 1**

**Mario pyramid**
"""

def print_right_triangle():
    Rows = int(input("Enter number of rows: "))
    for i in range(1, Rows + 1):
        space = Rows - i
        stars = i
        print(" " * space + "*" * stars)

def print_pyramid():
    height = int(input("Enter the desired pyramid height: "))
    for level in range(1, height + 1):
        stars = "*" * level
        spaces = " " * (height - level)
        print(spaces + stars)


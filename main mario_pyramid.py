# main mario_pyramid.py

import mario_pyramid

print("Choose a pattern:")
print("1. Right Triangle")
print("2. Pyramid")

choice = input("Enter 1 or 2: ")

if choice == "1":
    pyramids.print_right_triangle()
elif choice == "2":
    pyramids.print_pyramid()
else:
    print("Invalid choice.")

# Main.py

from multiplication_table import print_multiplication_tables, generate_multiplication_table

num = int(input("Enter the number to print multiplication tables: "))
print_multiplication_tables(num)

user_num = int(input("Enter your number to generate a table list: "))
table = generate_multiplication_table(user_num)
print("The multiplication table:", table)

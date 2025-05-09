# Main.py

from Email_user_input_module import simple_name_email_input, validated_name_email_input

print("Choose input method:")
print("1. Simple (name & email, basic check)")
print("2. Full validation (first & last name + validated email)")
choice = input("Enter 1 or 2: ")

if choice == '1':
    simple_name_email_input()
elif choice == '2':
    validated_name_email_input()
else:
    print("Invalid choice.")

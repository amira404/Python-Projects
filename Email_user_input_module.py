# Email_user_input_module.py

def simple_name_email_input():
    while True:
        name = input('Enter your name: ')
        if name.strip() and name.isalpha():
            print('Welcome', name)
            break
        else:
            print('Invalid name')

    email = input('Enter your email: ')
    if '@' in email and '.' in email:
        print('Welcome', email)
    else:
        print('Invalid email')


def validated_name_email_input():
    while True:
        first_name = input("Please Enter Your First Name: ").strip()
        if first_name.isalpha():
            break
        else:
            print("Enter a valid first name (letters only).")

    while True:
        last_name = input("Please Enter Your Last Name: ").strip()
        if last_name.isalpha():
            break
        else:
            print("Enter a valid last name (letters only).")

    print(f"Hello, {first_name} {last_name}")

    while True:
        email = input("Please Enter Your email: ").strip()
        if "@" in email and "." in email.split("@")[1]:
            try:
                username = email.split("@")[0]
                domain = email.split("@")[1].split(".")[0]
                tld = email.split("@")[1].split(".")[1]

                if username.isalpha() and domain.isalpha() and tld.isalpha():
                    print(f"Your Full Name Is: {first_name} {last_name} | Your Email Is: {email}")
                    break
                else:
                    print("Invalid email structure. Use letters only in username and domain.")
            except IndexError:
                print("Invalid email format. Please try again.")
        else:
            print("Invalid email format. Please include '@' and a domain.")

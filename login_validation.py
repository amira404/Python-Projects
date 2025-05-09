# login_validation.py

def login(data):
    user = input("Username: ").strip()

    if not user.isalpha():
        print("Invalid username")
    else:
        user_found = False
        for acc in data:
            if user == acc["name"]:
                user_found = True
                pwd = input("Password: ")
                if pwd == acc["password"]:
                    print(f"Logged in, {user}")
                else:
                    print("Wrong password")
                break
        
        if not user_found:
            print("Username not found")

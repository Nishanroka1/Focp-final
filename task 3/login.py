import hashlib

def authenticate_user(username, password):
    try:
        with open('passwd.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(':')

                # Check if the line has at least three parts
                if len(parts) >= 3 and parts[0] == username:
                    # Use MD5 for testing (not recommended for actual use)
                    encrypted_password = hashlib.md5(password.encode()).hexdigest()

                    print(f"Username: {username}")
                    print(f"Expected Password: {parts[2]}")
                    print(f"Entered Password: {encrypted_password}")

                    # Simple equality check
                    if encrypted_password == parts[2]:
                        return True
    
    except Exception as e:
        print(f"Error: {e}")

    return False

if __name__ == "__main__":
    username = input("User:     ")
    password = input("Password: ")

    if authenticate_user(username, password):
        print("Access granted.")
    else:
        print("Access denied.")
# passwd.py
import hashlib

def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    found = False
    with open('passwd.txt', 'w') as file:
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) >= 3 and parts[0] == username:
                found = True
                current_encrypted_password = hashlib.md5(current_password.encode()).hexdigest()
                if current_encrypted_password == parts[2]:
                    new_encrypted_password = hashlib.md5(new_password.encode()).hexdigest()
                    file.write(f'{parts[0]}:{parts[1]}:{new_encrypted_password}\n')
                    print('Password changed.')
                else:
                    print('Current password is invalid. No change made.')
            else:
                file.write(line)
    
    if not found:
        print('User not found. No change made.')

if __name__ == "__main__":  # Corrected "__main__"
    username = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")

    if new_password == confirm_password:
        change_password(username, current_password, new_password)
    else:
        print("Passwords do not match. No change made.")

import pyotp
import json
import os

# File to store 2FA codes
data_file = "2fa_codes.json"

# Load existing 2FA codes
def load_2fa_codes():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {}

# Save 2FA codes
def save_2fa_codes(codes):
    with open(data_file, "w") as file:
        json.dump(codes, file, indent=4)

# Add a new 2FA code using an existing secret key
def add_2fa():
    service_name = input("Enter the service name: ")
    secret = input("Enter the 2FA secret key: ").replace(" ", "").upper()
    codes = load_2fa_codes()
    codes[service_name] = secret
    save_2fa_codes(codes)
    print(f"2FA for {service_name} added successfully!")

# Delete an existing 2FA code
def delete_2fa():
    service_name = input("Enter the service name to delete: ")
    codes = load_2fa_codes()
    if service_name in codes:
        del codes[service_name]
        save_2fa_codes(codes)
        print(f"2FA for {service_name} deleted successfully!")
    else:
        print("Service not found!")

# View 2FA codes
def view_2fa():
    codes = load_2fa_codes()
    service_name = input("Enter the service name to view: ")
    if service_name in codes:
        totp = pyotp.TOTP(codes[service_name])
        print(f"2FA code for {service_name}: {totp.now()}")
    else:
        print("Service not found!")

def main():
    while True:
        print("\n2FA Manager")
        print("1. Add 2FA")
        print("2. Delete 2FA")
        print("3. View 2FA Codes")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_2fa()
        elif choice == '2':
            delete_2fa()
        elif choice == '3':
            view_2fa()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

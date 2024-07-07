def enter_password():
    # Define the password
    correct_password = "securepassword"

    # Ask the user to enter their password
    entered_password = input("Enter your password please: ")

    # Check if the entered password matches the correct password
    if entered_password == correct_password:
        print("Password accepted! You have access.")
    else:
        print("Incorrect password. Access denied.")

if __name__ == "__main__":
    enter_password()

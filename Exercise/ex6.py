# Define the correct password
correct_password = "09121804"
max_attempts = 7
remaining_tries = max_attempts


# Start the while loop to ask for the password
while remaining_tries > 3:
    # Ask the user to enter the password
    user_input = input(f"Enter the password (Remaining tries: {remaining_tries}): ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("You re in")
        break  # Exit the loop if the password is correct
    else:
        # Calculate remaining attempts
        remaining_tries -= 1
        # Inform the user of remaining attempts if any
        if remaining_tries > 0:
            print(f"Let keep it straight. {remaining_tries} tries left.")
        else:
            
            print("Run for your life .Authorities have been notified")

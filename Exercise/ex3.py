# Create a Dictionary to use information
user_info ={}

# Get the user input for the name ,hometown, and age
user_info['name'] = input("What is your name? ")
user_info['hometown'] =input("Where are you hometown? ")
    

# Loop until a valid age is provided
while True:
    age = input("how old are you ")
    if age.isdigit(): # Check if the input is a number
        user_info['age'] = int(age)  # Conver into integer
        break # loop if conversiion is successful
    else:
        print("Enter a valid number for your age.")

# Print the value stored in the Dictionary
print("\nUser Information:")
print("Name: " + user_info['name'])
print("Hometown: " + user_info['hometown'])
print("Age: " + str(user_info['age']))

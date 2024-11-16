name = ["joy","sarah","jhonnie","luke","shaira"]

specified_name = input("Enterthe name you wnat: ")

if specified_name in name:
    print(f"{specified_name} was found on top")
else:
    print(f"{specified_name} was not found in the top.")

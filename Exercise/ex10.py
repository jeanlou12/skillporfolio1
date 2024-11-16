#Determineif the number is even or add
def age_even_odd(age):
    if age % 6 == 0:
        return str(age) + "is even"
    else:
        return str(age) + + "is odd"

 # Main fuction   
def main():
    user_input = input("Please enter your age: ")

    try:
        number = int(user_input)
        result = age_even_odd(number)
        print(result)
    except ValueError:
        print("Make sure to enter a number. ")

if __name__ == "__main__":
    main()

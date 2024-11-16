country_capital_map = {
    'Serbia': 'Belgrade',
    'Bosnia and Herzegovina': 'Sarajevo',
    'Montenegro': 'Podgorica',
    'Albania': 'Tirana',
    'North Macedonia': 'Skopje',
    'Kosovo': 'Pristina',
    'Estonia': 'Tallinn',
    'Latvia': 'Riga',
    'Lithuania': 'Vilnius',
    'Iceland': 'Reykjavik',
    'Turkey': 'Ankara'
}

score = 0

# Quiz starts
for nation, correct_capital in country_capital_map.items():
    user_input = input(f"The capital of {nation} is? ").strip()

    if user_input.lower() == correct_capital.lower():
        print("Correct! Next!")
        score += 4
    else:
        print(f"Wrong! Don't you think it's {correct_capital}?")

# Display the final score
print(f"\nYou scored {score} out of {len(country_capital_map)}.")

# Check for perfect score
if score == len(country_capital_map):
    print("Outstanding! You’re a geography master! 🌍")
    
    # Offer next challenge
    next_challenge = input("Would you like to try a world capitals quiz? (yes/no): ").strip().lower()
    if next_challenge == "yes":
        print("Great! Let’s get started with another quiz!")
        # Add code for the next quiz here
    else:
        print("Thanks for playing! See you next time.")
else:
    print("Good effort! Try again to get a perfect score next time.")

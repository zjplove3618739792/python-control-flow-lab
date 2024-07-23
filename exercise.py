# 0.
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")


print_greeting()


# 1.
def check_letter():
    letter = input("Please enter a letter (a-z or A-Z): ").lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical letter.")


check_letter()

# 2.

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Invalid age. Age cannot be negative.")
        else:
            voting_age = 18
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not old enough to vote yet.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


check_voting_eligibility()



# 3.
def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age < 0:
            print("Invalid age. Age cannot be negative.")
        else:
            if dog_age <= 2:
                dog_years = dog_age * 10
            else:
                dog_years = 20 + (dog_age - 2) * 7
            print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


calculate_dog_years()


# 4.
def weather_advice():
    is_cold = input("Is it cold? (yes/no): ").strip().lower() == 'yes'
    is_raining = input("Is it raining? (yes/no): ").strip().lower() == 'yes'

    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")


weather_advice()


# 5.
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    try:
        day = int(input("Enter the day of the month: "))
        if month in ['Dec', 'Jan', 'Feb', 'Mar']:
            if (month == 'Dec' and day >= 21) or (month in ['Jan', 'Feb']) or (month == 'Mar' and day < 20):
                season = "Winter"
            else:
                season = "Spring"
        elif month in ['Mar', 'Apr', 'May', 'Jun']:
            if (month == 'Mar' and day >= 20) or (month in ['Apr', 'May']) or (month == 'Jun' and day < 21):
                season = "Spring"
            else:
                season = "Summer"
        elif month in ['Jun', 'Jul', 'Aug', 'Sep']:
            if (month == 'Jun' and day >= 21) or (month in ['Jul', 'Aug']) or (month == 'Sep' and day < 22):
                season = "Summer"
            else:
                season = "Fall"
        elif month in ['Sep', 'Oct', 'Nov', 'Dec']:
            if (month == 'Sep' and day >= 22) or (month in ['Oct', 'Nov']) or (month == 'Dec' and day < 21):
                season = "Fall"
            else:
                season = "Winter"
        print(f"{month} {day} is in {season}.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the day.")


determine_season()



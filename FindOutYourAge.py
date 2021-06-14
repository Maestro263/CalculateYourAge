def calculate_your_age():
    year_of_birth = int(input("Enter Your Year of Birth: "))
    birth_month = int(input("Enter your birth month (Number): "))
    your_age = 2021 - year_of_birth
    if birth_month <= 6:
        print("You are ", your_age, "years old")
    else:
        print("You are ", your_age - 1, "years old")


calculate_your_age()
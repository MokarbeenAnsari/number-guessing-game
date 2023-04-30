import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 25.")
    
    random_number = random.randint(1, 25)
    attempts = 0
    user_guess = -1

    while user_guess != random_number:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if user_guess < random_number:
            print("Higher! Try a larger number.")
        elif user_guess > random_number:
            print("Lower! Try a smaller number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()

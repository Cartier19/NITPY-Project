import random

def get_user_input(prompt):
    """Prompts the user for input and returns te entered value"""
    return input(prompt)


def generate_random_number():
    """Generates a random number between 1 and 100"""
    return random.randint(1, 100)


def get_user_guess():
    """Prompts the user to enter a guess amd returns the input as an integer """
    while True:
        try:
            guess= int(input("Enter your guess(1-100):"))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100")
        except ValueError:
            print("Invalud input. Please enter a number.")


def play_game():       
    """Plays the 'Guess the number' game"""
    print("Welcome to 'Guess the Number'!")
    secret_number = generate_random_number()
    attempts = 0
    name = get_user_input("Please enter your name")
    age = get_user_input("Please enter your age")

    print()

    while True:
        attempts+= 1
        guess = get_user_guess()

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts")  
            break


play_game()  
import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")

    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts to guess.")
            break

def main():
    play_again = True
    while play_again:
        guess_number()
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == "yes"

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

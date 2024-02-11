import random
import string

def generate_password(length=12):
    """Generate a strong password with the specified length."""
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))

    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()

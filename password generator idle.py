import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters   # a-z + A-Z
    if use_digits:
        characters += string.digits          # 0-9
    if use_symbols:
        characters += string.punctuation     # !@#$...

    if characters == "":
        return "Error: No character types selected!"

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Random Password Generator ===")

    # Get password length
    length = int(input("Enter password length: "))

    # Ask user preferences
    letters = input("Include letters? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, letters, digits, symbols)

    print("\nGenerated Password:", password)


# Run program
main()

import random
import string

length = int(input("Enter the length of the password: "))
character_set = input("Enter the character set to use for the password (letters, numbers, symbols, or all): ").lower()


def generate_password(length, character_set):
    if character_set == 'letters':
        characters = string.ascii_letters
    elif character_set == 'numbers':
        characters = string.digits
    elif character_set == 'symbols':
        characters = string.punctuation
    elif character_set == 'all':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid character set")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def your_password():
    password = generate_password(length, character_set)
    print(f"Your password: {password}")

if __name__ == '__main__':
    your_password()
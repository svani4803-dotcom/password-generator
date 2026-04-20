import random
import string


def generate_password(length, use_digits, use_symbols):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = lower + upper + digits + symbols

    # Ensure at least one of each required type
    password = [
        random.choice(lower),
        random.choice(upper)
    ]

    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill remaining length
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to avoid pattern
    random.shuffle(password)

    return ''.join(password)


def save_to_file(passwords):
    with open("passwords.txt", "a") as file:
        for pwd in passwords:
            file.write(pwd + "\n")


def main():
    print("🔐 PASSWORD GENERATOR 🔐\n")

    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length < 4:
                print("Length must be at least 4\n")
                continue

            count = int(input("How many passwords to generate? "))

            digits = input("Include numbers? (y/n): ").lower() == 'y'
            symbols = input("Include symbols? (y/n): ").lower() == 'y'

            passwords = []

            print("\nGenerated Passwords:\n")

            for _ in range(count):
                pwd = generate_password(length, digits, symbols)
                passwords.append(pwd)
                print(pwd)

            save = input("\nSave passwords to file? (y/n): ").lower()
            if save == 'y':
                save_to_file(passwords)
                print("Saved to passwords.txt")

            again = input("\nGenerate again? (y/n): ").lower()
            if again != 'y':
                print("Thank you 👍")
                break

        except ValueError:
            print("Invalid input! Please enter numbers correctly.\n")


if __name__ == "__main__":
    main()
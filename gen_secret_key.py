import os
import sys
from django.core.management.utils import get_random_secret_key


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'SECRET KEY GENERATOR - Django'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    print("Your new Django secret key:\n")
    print(get_random_secret_key())

    while True:
        response = input('\nGenerate another? (Y/N) ')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print("Thank you and happy coding.\n")
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')
            continue

if __name__ == '__main__':
    main() 
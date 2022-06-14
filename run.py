import gspread
import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Enter_the_Matrix')

class colors:
    GREEN = '\033[92m'
    WHITE = '\033[97m'

def welcome():
    """
    Welcome message.
    """
    print("\n\n")
    print("=" * 70)
    print("Hello and welcome to this very useful matrix determinant finder tool!")
    print("=" * 70)
    print("\n                               Enter the")
    print(colors.GREEN + "              __  __           _            _        ")
    print(colors.GREEN + "             |  \/  |   __ _  | |_   _ __  (_) __  __")
    print(colors.GREEN + "             | |\/| |  / _` | | __| | '__| | | \ \/ /")
    print(colors.GREEN + "             | |  | | | (_| | | |_  | |    | |  >  < ")
    print(colors.GREEN + "             |_|  |_|  \__,_|  \__| |_|    |_| /_/\_\ ")
    print(colors.WHITE + " ")
    print("=" * 70)
    print("")
    print("=" * 70)
    start_menu()

def start_menu():
    """
    Create username or login.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - create username")
    print("2 - login")
    start_input = input()
    if start_input == "1":
        clear_console()
        print("\n\nLoading...\n\n")
        create_user()
    elif start_input == "2":
        clear_console()
        login_user()
    else:
        print(f"\nYou entered: {start_input}. Please enter 1 or 2.")
        start_menu()

def create_user():
    """
    Validate the username input.
    """
    purge()
    print("Done!\n\n")
    login = SHEET.worksheet('login')
    login_col = login.col_values(1)
    new_user = input("Please type in a new username: ")
    if new_user in login_col:
        clear_console()
        print("\n\nUsername already exist. Please enter another one.\n")
        retry_new_user()
    else:
        print("\nUsername available.\n")
        free_cell = list(filter(None, login_col))
        up = str(len(free_cell) + 1)
        login.update_cell(up, 1, new_user)
        new_pass()

def purge():
    """
    Purge the username cell if password is missing for it.
    """
    login = SHEET.worksheet('login')
    password = SHEET.worksheet('pass')
    login_col = login.col_values(1)
    pass_col = password.col_values(1)

    last_login = list(filter(None, login_col))
    last_login_n = str(len(last_login))

    last_pass = list(filter(None, pass_col))
    last_pass_n = str(len(last_pass))

    if last_login_n != last_pass_n:
        login.update_cell(last_login_n, 1, "")

def new_pass():
    """
    Create a password once username is created.
    """
    password = SHEET.worksheet('pass')
    pass_col = password.col_values(1)
    newpass = input("Please type in a new password: ")
    free_cell = list(filter(None, pass_col))
    up = str(len(free_cell) + 1)
    password.update_cell(up, 1, newpass)
    clear_console()
    print('\n\nCredentials sucessfully created!')
    creds_created()

def creds_created():
    """
    Navigate to login or to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - login")
    print("2 - return to the main screen")
    creds_create = input()
    if creds_create == "1":
        clear_console()
        login_user()
    if creds_create == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {creds_create}. Please enter 1 or 2.")
        creds_created()

def retry_new_user():
    """
    Retry creating new username or
    return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - retry new username")
    print("2 - return to the main screen")
    retry_new_name_input = input()
    if retry_new_name_input == "1":
        clear_console()
        print("\n\nLoading...\n\n")
        create_user()
    elif retry_new_name_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {retry_new_name_input}. Please enter 1 or 2.")
        retry_new_user()

def login_user():
    """
    Display the login message and validate the user/password input.
    """
    login_input = input('\nType in the username: ')
    login = SHEET.worksheet('login')
    password = SHEET.worksheet('pass')
    login_col = login.col_values(1)
    while True:
        try:
            if login_input not in login_col:
                print(f'No such user "{login_input}" exists.')
                retry_name()
            else:
                print('Username correct.\n')
                login_cell = login.find(login_input)
                pass_input = input('Type in password: ')
                pass_cell = password.cell(login_cell.row, 1).value
                if pass_input != pass_cell:
                    print('\nIncorrect password.\n')
                    retry_pass()
                else:
                    clear_console()
                    print('\nLogin successful!\n\n')
                    how_to()
            return
        except ValueError():
            print('Invalid data. Please try again.')
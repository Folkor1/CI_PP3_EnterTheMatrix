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


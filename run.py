import gspread
import os
from google.oauth2.service_account import Credentials

from matrix import Matrix_2x2
from matrix import Matrix_3x3
from matrix import Matrix_4x4

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
    text_a = "Hello and welcome to this "
    text_b = "very useful matrix determinant finder tool!"
    text_c = "             "
    print("=" * 70)
    print(text_a + text_b)
    print("=" * 70)
    print("\n                              Enter the")
    print(colors.GREEN + text_c + " __  __           _            _        ")
    print(colors.GREEN + text_c + "|  \/  |   __ _  | |_   _ __  (_) __  __")
    print(colors.GREEN + text_c + "| |\/| |  / _` | | __| | '__| | | \ \/ /")
    print(colors.GREEN + text_c + "| |  | | | (_| | | |_  | |    | |  >  < ")
    print(colors.GREEN + text_c + "|_|  |_|  \__,_|  \__| |_|    |_| /_/\_\ ")
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
    new_user = input("Please type in a new username:\n ")
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
    newpass = input("Please type in a new password:\n ")
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
                pass_input = input('Type in password:\n ')
                pass_cell = password.cell(login_cell.row, 1).value
                if pass_input != pass_cell:
                    print('\nIncorrect password.\n')
                    retry_pass()
                else:
                    clear_console()
                    print('Login successful!\n\n')
                    how_to()
            return
        except ValueError():
            print('Invalid data. Please try again.')


def retry_name():
    """
    Retry login if login is incorrect,
    or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - retry login")
    print("2 - return to the main screen")
    retry_name_input = input()
    if retry_name_input == "1":
        clear_console()
        login_user()
    elif retry_name_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {retry_name_input}. Please enter 1 or 2.")
        retry_name()


def retry_pass():
    """
    Retry login if password is incorrect,
    or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - retry login")
    print("2 - return to the main screen")
    retry_pass_input = input()
    if retry_pass_input == "1":
        clear_console()
        login_user()
    elif retry_pass_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {retry_pass_input}. Please enter 1 or 2.")
        retry_pass()


def clear_console():
    """
    Clear the console.
    """
    clear = os.system('clear')


def how_to():
    """
    Show 'How to' text and the logged-in menu.
    """
    print('=' * 80)
    print('\nHow to:')
    print('\nEnter 2, 3 or 4 numbers, separated by comma.')
    print('\nDepending on your input, the programm will')
    print('request next batch of numbers - 2, 3 or 4.')
    print('\nFor example, if you entered 3, then the program ')
    print('will request 3 more numbers 2 more times.')
    print('\nThen the program will return the matrix and its determinant.')
    print('\nExample:\n')
    print(colors.GREEN + '   3   4   5')
    print(colors.GREEN + '   0   8   1')
    print(colors.GREEN + '   9   7   6')
    print(colors.WHITE + '   \nThe matrix determinant is: -201')
    print('=' * 80)
    logged_in_menu()


def logged_in_menu():
    """
    Call the matrix building function or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - start")
    print("2 - return to the main screen")
    logged_input = input()
    if logged_input == "1":
        build()
    elif logged_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {logged_input}. Please enter 1 or 2.")
        logged_in_menu()


def build():
    """
    Get the matrix input then calculate and display
    the determinant.
    """
    buildm = start()
    clear_console()
    print("\n\n" + "=" * 32)
    print(f"Here is your {len(buildm)}x{len(buildm)} matrix:\n")
    for i in range(len(buildm)):
        print(colors.GREEN + "      " + buildm[i].replace(",", "  "))
    array = str(buildm).replace("[", "").replace("'", "").replace("]", "")
    array = tuple(map(int, array.split(',')))
    text = "\nThe matrix determinant is: "
    if len(array) == 4:
        calc_2x2 = Matrix_2x2(*array)
        print(colors.WHITE + text + f'{calc_2x2.determinant_2x2()}')
    if len(array) == 9:
        calc_3x3 = Matrix_3x3(*array)
        print(colors.WHITE + text + f'{calc_3x3.determinant_3x3()}')
    if len(array) == 16:
        calc_4x4 = Matrix_4x4(*array)
        print(colors.WHITE + text + f'{calc_4x4.determinant_4x4()}')
    print("=" * 32)
    try_again()


def try_again():
    """
    Build another matrix or return to the main screen.
    """
    print('\n\nSelect one of the following options:')
    print("\n1 - try again")
    print("2 - return to the main screen")
    try_again_input = input()
    if try_again_input == "1":
        clear_console()
        build()
    elif try_again_input == "2":
        clear_console()
        welcome()
    else:
        print(f"\nYou entered: {try_again_input}. Please enter 1 or 2.")
        try_again()


def start():
    """
    Get the list of numbers depending on the first input,
    i.e. amount of numbers entered in each input should match.
    """
    clear_console()
    print('\n\nStarting...')
    print('\nReady!')
    matrix = []
    while True:
        print('\nEnter 2, 3 or 4 numbers, separated by comma:')
        matrix_input = input()
        matrix_data = matrix_input.split(',')
        if validate_first_input(matrix_data):
            matrix.append(matrix_input)
            while True:
                print(f"\nEnter another {len(matrix_data)} numbers:")
                next_input = input()
                next_data = next_input.split(',')
                if validate_next(matrix_data, next_data):
                    matrix.append(next_input)
                    if len(matrix) == len(matrix_data):
                        return matrix


def validate_first_input(values):
    """
    Validate the first input, whether 2, 3 or 4 numbers are entered.
    """
    try:
        [int(value) for value in values]
        if len(values) not in range(2, 5):
            print(f"\nPlease enter 2, 3 or 4 only. You entered: {len(values)}")
        else:
            return True
    except ValueError as e:
        print(f"{e}. Please try again.")
        return False


def validate_next(value1, value2):
    """
    Validate next after the first inputs.
    """
    try:
        [int(val1) for val1 in value1]
        [int(val2) for val2 in value2]
        if len(value1) != len(value2):
            val2 = (f"You entered: {len(value2)}")
            print(f"\nPlease enter {len(value1)} numbers. " + val2)
        else:
            return True
    except ValueError as e:
        print(f"{e}. Please try again.")
        return False


welcome()

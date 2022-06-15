# Enter The Matrix

**Developer: Igor Vasiljev**

[Link to the live project](https://type-the-matrix.herokuapp.com/)

![logo](assets/docs/Logo.PNG)

## About

'Enter the Matrix' program accepts a user input of 2, 3 or 4 lines of numbers, then builds and returns the matrix and its determinant.
The program also allows to create a unique user login and password.

The tool's objective is to help the user with math calculations of finding 2x2, 3x3 or 4x4 matrix determinant.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Ability to create an account.
- Run math calculations and get the results.

### Site Owner Goals

- Create a useful tool with clear and understandable objectives.
- Easy to use, user friendly and intuitive navigation.

## User Experience

### Target Audience

- Everyone who's aware of what matrices and their determinants are.

### User Requirements and Expectations

- Easy navigation.
- Clear program responce to the user input.
- Non-bulky texts.
- Correct math results of the program.

### User Manual

<details><summary>Click here to view instructions</summary>

### Main Menu
On the main menu screen the program logo is displayed, and the user will have 2 options here - create a new username or use an existing login information.

Options:
- create username
- login

### Create username
First the user has an input line to enter a new username. 

Input name:
- Please type in a new username

If existing username is entered, then the program will notify the user about it and ask to enter another user name, or return to the main menu.

Options:
- retry new username
- return to the main screen

Once the user name is created, the program will ask to enter a password. If the program will be terminated at this point, then the username will be purged from the data base on the next run.

Input password:
- Please type in a new password

When user name and password are created, the user can either login or return to the main screen.

Options:
- login
- return to the main screen

### Login
Login option can be used when the user has created the user name and password.

Input:
- Type in the username

If the user name entered is incorrect, the program will notify the user and give 2 options:

- retry login
- return to the main screen

In case if user name is entered correctly, then the user is asked to type in the password:

- Type in password

And if the password is entered incorrectly, the user will need to start authentication process from the beginning:

- retry login
- return to the main screen

### Login successful
When the user successfully logs in, the information window will be displayed with a brief description of how to use the program and the example. Apart from that there 2 options:

- start
- return to the main screen

### Start
Once the program started the user is advised to enter 2, 3 or 4 numbers, separated by comma. If the input is invalid, the corresponding error message will be returned.
If 2 numbers are entered first, then the program will request another 2 numbers in the next input. As before, in case of incorrect input the error message will be returned. Same for 3 and 4 numbers.

Once the final batch of numbers is entered, the program will process the overall input and return the matrix and calculate its determinant using the corresponding math formulas.

The the program will ask if user wishes to run the program again, or return to the main screen:

- try again
- return to the main screen

</details>

## User Stories

### Users

1. As a user I want to have a functionality to create a new user name and password.
2. I want to have an ability to use existing user name and password.
3. I want to have a clear undestanding of what went wrong in the case of error.
4. I want to have understandable, non-bulky instructions of use.
5. I want to be able to easily navigate from any point of the program to the main menu.
6. I want to run the program and get the correct results based on my input.
7. I want to have an ability to repeat the program multiple times without re-logging.

### Site Owner

1. As a site owner I want the users to have a perfect understanding of what the program do.
2. I want the users to have positive experience.
3. I want the users to avail from the program math functionality.

## Technical Design

### Flowchart
The following flowchart represents the matrix input and calculation program logic:

<details><summary>Flowchart</summary>

![Flowchart](assets/docs/Flowchart.jpeg)

</details>


# vityarthi-project-simple-calculator
Simple Python Calculator

Overview of the Project

This project is a Command Line Interface (CLI) based calculator built using Python.
It enables users to carry out basic arithmetic functions like adding, subtracting, multiplying, and dividing numbers. The program operates in a loop, allowing users to do several calculations during a single session without needing to restart. It also includes simple error checking to handle situations where users input non-numeric values or attempt to divide by zero.

Features

Arithmetic Operations: The calculator supports addition, subtraction, multiplication, and division.


Continuous Usage: A while loop keeps the program running, letting users perform multiple calculations in one session.


Error Handling: The system can detect if a user inputs letters instead of numbers.


Prevents crashing when dividing by zero.


User-Friendly Interface: It offers a clear menu and exit commands for easy navigation.


Technologies/Tools Used

Language: Python 3.x

IDE/Editor: VS Code / IDLE (or any other editor you prefer)

Version Control: Git & GitHub

Steps to Install & Run the Project

Clone the Repository:

Open your terminal or command prompt and run:

git clone [https://github.com/YourUsername/Your-Repo-Name.git](https://github.com/YourUsername/Your-Repo-Name.git)

Navigate to the Directory:

cd Your-Repo-Name

Run the Application:

Make sure you have Python installed.
Run the command:

python calculator.py

Instructions for Testing

To test the calculator, follow these scenarios:

Test Addition:

Run the program.


Select option 1.


Input 10 and 5.


Expected Output: Result: 15.0

Test Division by Zero:

Select option 4.


Input 10 as the first number and 0 as the second.


Expected Output: Error!
Division by zero.

Test Invalid Input:

Select any operation.


Enter abc instead of a number.


Expected Output: Invalid input!
Please enter numeric values.

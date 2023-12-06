# Casino Python Game

This simple Python program simulates a casino game where players can choose their risk level and play a coinflip game.

## How to Play

    1. Run the Program:
        Ensure that you have Python installed on your machine.
        Download the casino_game.py file.
        Open a terminal and navigate to the directory containing the script.
        Run the program using the command: python casino_game.py.

    2. Enter Player Information:
        Enter a name for the player when prompted.
        Choose a risk level (low, medium, or high) when prompted.

    3. Game Options:
        The program will display the starting cash based on the chosen risk level.
        Choose between playing a coinflip game or checking your account balance.
        Follow the on-screen instructions to enter the amount you want to bet in the coinflip game and choose heads or tails.

    4. Play or Check Balance:
        After each game, the program will display the result and your current cash balance.
        Choose to play another game, check your balance, or exit the program.

    5. Exit the Program:
        Type 'end' when prompted to exit the program.

# Player Classes
The program defines three player classes with different risk levels: Easy Goer (low), Conservative Chap (medium), and High Roller (high).

# Dependencies
The program uses the random and sys modules, which are part of the Python standard library.

# Notes
This program is a simple text-based simulation and does not involve actual monetary transactions.
Ensure you have Python installed on your machine before running the program.

Feel free to explore and have fun in the virtual casino!


# Python Skills Demonstrated
1. Object-Oriented Programming (OOP)

    Classes and Instances:
        The program uses object-oriented programming concepts with the Players class. Each player is an instance of this class, encapsulating attributes like name, level, cash, and current_cash.

    Constructor (__init__ method):
        The __init__ method initializes the object's attributes when a new player instance is created.

    Class Methods:
        The account_check and coinflip methods are class methods that encapsulate behavior related to checking account balances and playing the coinflip game, respectively.

2. User Input Handling

    input() Function:
        User input is captured using the input() function, allowing users to interactively provide their name, choose a risk level, and input game-related choices.

3. Random Module

    random Module:
        The random module is utilized to generate a random outcome (heads or tails) for the coinflip game. The random.choice([0, 1]) expression randomly selects either 0 or 1.

4. Conditional Statements

    if, elif, and else Statements:
        Conditional statements are used to validate user inputs and determine the outcome of the coinflip game. For example, the program checks whether the user entered 'heads' or 'tails' and adjusts the game accordingly.

5. Looping Structures

    while Loop:
        The main gameplay loop is governed by a while True loop, allowing the player to continue playing or checking their balance until they decide to exit.

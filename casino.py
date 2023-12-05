import random
import sys

class Players:
    def __init__(self, input_name, input_level,input_cash, current_cash=0):
        self.name = input_name
        self.level = input_level
        self.cash = input_cash
        self.current_cash = current_cash + input_cash

    def account_check(self):
        amount = self.current_cash
        return "{name} has {cash} left in their account.".format(name = self.name, cash = amount)

    def coinflip(self):
        money_input = int(input("How much would you like to bet? "))
        choice_input = input("Choose heads or tails:")
        random_int = random.choice([0,1])
        
        if choice_input == 'heads':
            the_input = 0
        elif choice_input == 'tails':
            the_input = 1
        else:
            print("Invalid choice. Please choose heads or tails: ")
            return
            
        if the_input == random_int:
            self.current_cash += (money_input * 2)
            return "Winner! Current cash = {cashy}".format(cashy = self.current_cash)
        else:
            self.current_cash -= (money_input * 2)
            return "You lost sorry :(. Current cash = {cashy}".format(cashy = self.current_cash)

a = Players("Easy Goer", "low", 0, 10)
b = Players("Conservative Chap", "medium", 0, 100)
c = Players("High Roller", "high", 0, 1000)




player_name = input("Welcome to the Casino. Please enter a name for player and hit enter: ")
choice = input("Hello, " + player_name + "! Choose your risk level (low, medium or high) and hit enter: ")

while choice != 'high' and choice != 'medium' and choice != 'low':
    choice = input("Oopsies, it looks like we didn't recognize your input. Try selecting low, medium or high and hit enter! ")

player_one = []

if choice == 'low':
    player_one.append(a)
    print("You are the Easy Goer! Starting cash is $10")
elif choice == 'medium':
    player_one.append(b)
    print("You are the Conservative Chap! Starting cash is $100")
else:
    player_one.append(c)
    print("You are the High Roller! Starting cash is $1000")


print("Let's get ready to play! ")

while True:
    game = input("Choose a game (coinflip) or type balance, and hit enter: ")
    if game == "coinflip":
        result = player_one[0].coinflip()
        print("$" + result + " currently in your account. ")
    elif game == "balance":
        result = player_one[0].account_check()
        print("$" + result + " currently in your account. ")
    else:
        print("Unknown answer please try again, coinflip or balance? ")

    new_choice = input("Type 'game' to play another game or 'balance' to see your current balance, or type 'end' to exit: ")
    if new_choice.lower() == "end":
        print("Exiting the program. Goodbye!")
        sys.exit()
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
            print(" Invalid choice. Please choose heads or tails: ")
            return
            
        if the_input == random_int:
            self.current_cash += (money_input * 2)
            return " Winner! Current cash = {cashy} ".format(cashy = self.current_cash)
        else:
            self.current_cash -= (money_input * 2)
            return " You lost sorry :(. Current cash = {cashy} ".format(cashy = self.current_cash)

    
    def slots(self):
        money_input = int(input(" How much would you like to bet? "))
        random_int1 = random.choice([0,2])
        random_int2 = random.choice([0,2])
        random_int3 = random.choice([0,2])
        
        if random_int1 == random_int2 and random_int1 == random_int3:
            self.current_cash += money_input * 0.5
            print("${cashy} currently left in your account. ".format(cashy=self.current_cash))
        elif random_int1 == 1 and random_int2 == 2 and random_int3 == 3:
            self.current_cash += money_input * 100
            print(" Jackpot! Winnings multiplied by 100!")
            print("${cashy} currently left in your account. ".format(cashy=self.current_cash))
        else:
            self.current_cash -= money_input
            return " Not a match! Your current balance is: ${cash} ".format(cash = self.current_cash)
    
    
    def baccarat(self):
        
        # standard card deck with numbers assigned per baccarat rules
        deck = {"1H":1,"2H":2,"3H":3,"4H":4,"5H":5,"6H":6,"7H":7,"8H":8,"9H":9,"10H":0,"JH":0,"QH":0,"KH":0,"AH":1,"1S":1,"2S":2,"3S":3,"4S":4,"5S":5,"6S":6,"7S":7,"8S":8,"9S":9,"10S":0,"JS":0,"QS,":0,"KS":0,"AS":1,"1C":1,"2C":2,"3C":3,"4C":4,"5C":5,"6C":6,"7C":7,"8C":8,"9C":9,"10C":0,"JC":0,"QC":0,"KC":0,"AC":1,"1D":1,"2D":2,"3D":3,"4D":4,"5D":5,"6D":6,"7D":7,"8D":8,"9D":9,"10D":0,"JD":0,"QD":0,"KD":0,"AD":1}
        result = 0
        
        # two cards are drawn from the above deck for each player
        bank_draw1 = deck[random.choice(list(deck.keys()))]
        bank_draw2 = deck[random.choice(list(deck.keys()))]
        player_draw1 = deck[random.choice(list(deck.keys()))]
        player_draw2 = deck[random.choice(list(deck.keys()))]

        player_total = player_draw1 + player_draw2
        banker_total = bank_draw1 + bank_draw2

        if player_total == 0 and banker_total == 0:
            banker_total += random.choice([deck])
            player_total += random.choice(deck)
        elif player_total >= 10 or banker_total >= 10:
            player_total -= 10
            banker_total -= 10

        # player or bank wins if they are closer to 9 aka whoever has a higher number
        player_win = (bank_draw1 + bank_draw2) < (player_draw1 + player_draw2)
        bank_win = (bank_draw1 + bank_draw2) > (player_draw1 + player_draw2)
        both_win = (bank_draw1 + bank_draw2) == (player_draw1 + player_draw2)


        money_input = int(input(" How much would you like to bet? "))
        bet_input = input(" Please enter one of the following to place your bet: player, banker, tie, tie player, tie banker: ")
        


             # bet types and money return rules
        if bet_input == 'player':
            if player_win == True or both_win == True:
                self.current_cash = self.current_cash + (money_input * 2)
                return " Player wins! Current Balance: ${cashy} ".format(cashy=self.current_cash)
            elif player_win == False:
                self.current_cash = self.current_cash - money_input
                return " Player loses :( Current Balance: ${cashy} ".format(cashy=self.current_cash)
        elif bet_input == 'banker':
            if bank_win == True or both_win == True:
                self.current_cash = self.current_cash + (money_input * 2)
                return " Banker wins! Current Balance: ${cashy} ".format(cashy=self.current_cash)
            elif player_win == False:
                self.current_cash = self.current_cash - money_input
                return " Banker loses :( Current Balance: ${cashy} ".format(cashy=self.current_cash)
        elif bet_input == 'tie':
            if both_win == True:
                self.current_cash = self.current_cash + (money_input * 8)
                return " Tie wins! Current Balance: ${cashy} ".format(cashy=self.current_cash)
            else: self.current_cash = self.current_cash - money_input
            return " Tie loses :( Current Balance: ${cashy} ".format(cashy=self.current_cash)
        elif bet_input == 'tie player':
            if player_draw1 == player_draw2:
                self.current_cash = self.current_cash + (money_input * 11)
                return " Tie Player wins! Current Balance: ${cashy} ".format(cashy=self.current_cash)
            else: self.current_cash = self.current_cash - money_input
            return " Tie Player loses :( Current Balance: ${cashy} ".format(cashy=self.current_cash)
        elif bet_input == 'tie banker':
            if bank_draw1 == bank_draw2:
                self.current_cash = self.current_cash + (money_input * 11)
                return " Tie Banker wins! Current Balance: ${cashy} ".format(cashy=self.current_cash)
            else: self.current_cash = self.current_cash - money_input
            return " Tie Banker loses :( Current Balance: ${cashy} ".format(cashy=self.current_cash)
        else: print(" Bet input not recognized. Try again: ")
        return " Bet input not recognized. Try again: "


        

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
    print(" You are the Easy Goer! Starting cash is $10")
elif choice == 'medium':
    player_one.append(b)
    print(" You are the Conservative Chap! Starting cash is $100")
else:
    player_one.append(c)
    print(" You are the High Roller! Starting cash is $1000")


print(" Let's get ready to play! ")

while True:
    game = input(" Choose a game (coinflip, slots, baccarat) to choose a game, type balance to check your current balance, or type end to exit the game and hit enter: ")
    if game == "coinflip":
        result = player_one[0].coinflip()
        print(result)
    elif game == "slots":
        result = player_one[0].slots()
        print(result)
    elif game == "balance":
        result = player_one[0].account_check()
        print(result)
    elif game == "baccarat":
        result = player_one[0].baccarat()
        print(result)
    elif game == "end":
        print("Exiting the program. Goodbye!")
        sys.exit()
    else:
        print("Unknown answer please try again, coinflip, slots or balance? ")

new_choice = input(" Type 'game' to play another game or 'balance' to see your current balance, or type 'end' to exit: ")
if new_choice.lower() == "end":
    print("Exiting the program. Goodbye!")
    sys.exit()


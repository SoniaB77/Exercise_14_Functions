import random

# Things to consider: ROCK, PAPER, SCISSORS.
# - User input which only accepts values of R,P or S which correlate to Rock, Paper, Scissors.
# - Have the computer randomly select rock, paper or scissors.
# - Need variables to display the user wins along with the computer wins and any draws.
#   ~ consider a while loop to compare player wins and computer wins??
#   ~ need to track the wins and print the results - display message??
#   ~ option to ask the user if they want to keep playing or exit the game.
# - Remember Rock smashes Scissors, Paper wraps Rock, Scissors cut Paper!

welcome_user = input("Please enter your name: ").capitalize()
print("Hello", welcome_user)

def player_moves():
    user_input = input("Please enter your move of either Rock, Paper or Scissors: ").lower()

    comp_options = {0: "rock", 1: "paper", 2: "scissors"}
    comp_choice = comp_options.get(random.randint(0, 2))

    winner = ""

    if user_input in ["rock", "r"]:
        if comp_choice == "rock":
            print(f"{welcome_user}, you chose rock. The computer also chose rock. You have tied.")
            winner = "tie"
        elif comp_choice == "paper":
            print(f"You chose rock. The computer chose paper. Sorry {welcome_user}, you've lost this time.")
            winner = "comp"
        elif comp_choice == "scissors":
            print(f"You chose rock. The computer chose scissors. You won. Well done {welcome_user}.")
            winner = "user"

    elif user_input in ["paper", "p"]:
        if comp_choice == "rock":
            print(f"You chose paper. The computer chose rock. You won. Well done {welcome_user}.")
            winner = "user"
        elif comp_choice == "paper":
            print(f"{welcome_user}, you chose paper. The computer also chose paper. You have tied.")
            winner = "tie"
        elif comp_choice == "scissors":
            print(f"You chose paper. The computer chose scissors. Sorry {welcome_user}, you've lost this time.")
            winner = "comp"

    elif user_input in ["scissors", "s"]:
        if comp_choice == "rock":
            print(f"You chose scissors. The computer chose rock. Sorry {welcome_user}, you've lost this time.")
            winner = "comp"
        elif comp_choice == "paper":
            print(f"You chose scissors. The computer chose paper. You won. Well done {welcome_user}.")
            winner = "user"
        elif comp_choice == "scissors":
            print(f"{welcome_user}, you chose scissors. The computer also chose scissors. You have tied.")
            winner = "tie"

    else:
        print(f"Input not valid. Please try again {welcome_user}. Enter your move of rock, paper or scissors.")
    return winner


user_tally = 0
comp_tally = 0
tie_tally = 0

user_play = True
while user_play:
    round_winner = player_moves() # starts a round, returns value of winner.
    if round_winner == "user": # checks who winner is, tallies it.
        user_tally += 1
    elif round_winner == "comp":
        comp_tally += 1
    elif round_winner == "tie":
        tie_tally +=1
    user_play = True if input(f"Would you like to play again {welcome_user} ? ").lower() in ["yes", "y"] else False #checks if user wants to play again.

if user_tally > comp_tally: # compares total scores to see who won overall and displays message.
    print(f"You scored {user_tally}. Well done {welcome_user}. You won!")
elif user_tally < comp_tally:
    print(f"You scored {user_tally}. The computer scored {comp_tally} You lose. Better luck next time {welcome_user}.")
elif user_tally == comp_tally:
    print(f"You scored {user_tally}. The computer scored {comp_tally}. You tied. You did alright {welcome_user}.")

input("Press return to close") # stops the command line window from closing suddenly after game ends.

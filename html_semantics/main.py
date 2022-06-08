# Rock Paper and Scissors Game
# Start

from random import choice
from time import sleep

# msg()
def msg():
    info = """
Rock Paper Scissors
A simultaneous, zero-sum games, it has three possible outcomes: a draw, a win or loss. 
A player who decides to play rock will beat another player who has chosen scissors 
('rock crushes scissors' or 'breaks scissors' or sometimes 'blunts scissors'),
but will lose to one who played paper ('paper covers rock'): a play of paper
will lose to a play of scissors ('scissors cuts paper'). If both players choose the same
shaper, the game is tied and is immediately replayed to break the tie. \nStart... \n"""
    return info
print(msg())

player = (input("Pick an option from 'R' for 'Rock', 'P' for 'Paper, or 'S' for 'Scissors': ")).upper() # player
options = ['R', 'P', 'S'] # list of options
cpu = choice(options) # CPU

# win or loss
def beats(player, cpu):
    players = player, cpu
    if 'R' in players and 'S' in players:
            if player == 'R':
                return f"Player(Rock): CPU(Scissor) \nPlayer wins "
            else:
                return f"Player(Scissors): CPU(Rock) \nCPU wins "
    elif 'R' in players and 'P' in players:
        if player == 'P':
            return f"Player(Paper): CPU(Rock) \nPlayer wins "
        else:
            return f"Player(Rock): CPU(Paper) \nCPU wins "
    else:
        if player == 'S':
            return f"Player(Scissors): CPU(Paper) \nPlayer wins "
        else:
            return f"Player(Paper): CPU(Scissor) \nCpu wins "

# wrong input
def wrong_input(player):
    while True:
        info = f"Oopss!, '(player)' is not among the options... Try again"
        if player in options:
            return player
        else:
            sleep(1)
            print(info)
            player = (input("Pick an option from 'R' for 'Rock', 'P' for 'Paper, or 'S' for 'Scissors': ")).upper()

# Tie
def tie(player, cpu):
    while True:
        if player != cpu:
            return player, cpu
        else:
            sleep(1)
            print(f"Player(Rock): CPU(Rock)") if player == 'R' else None
            print(f"Player(Paper): CPU(Paper)") if player == 'P' else None
            print(f"Player(Scissors): CPU(Scissors)") if player == 'S' else None
            print("It is a tie...Try again")
            player = (input("Pick an option from 'R' for 'Rock', 'P' for 'Paper, or 'S' for 'Scissors': ")).upper()
            cpu = choice(options)

# Game
def rock_scissor_paper(player, cpu):
    if player in options:
        sleep(1)
        return beats(player, cpu)
    else:
        player = wrong_input(player)
        return beats(player, cpu)

# Testing
if player == cpu:
    player, cpu = tie(player, cpu)
    print(rock_scissor_paper(player, cpu))
else:
    print(rock_scissor_paper(player, cpu))

print("\n...End") # End                                 
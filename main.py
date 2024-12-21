import random


PLAYER = 'p'
COMPUTER = 'c'
tie = 't'
outcome = []
# optimised code to not need to track 2 lists and instead rely on 1
# current_winner = []

def winner(outcome):
    if outcome[-2:] == ['p', 'p']:
        print('Player WINS!')
        return True
    elif outcome[-2:] == ['c', 'c']:
        print('Computer WINS!')
        return True
    
def winning_move(player_move_lowercase, computer_move):
    if player_move_lowercase == computer_move:
        outcome.append(tie)
        # current_winner.append('Tie')
        
    
    elif (
        (player_move_lowercase == 'rock' and computer_move == 'scissors') or
        (player_move_lowercase == 'paper' and computer_move == 'rock') or
        (player_move_lowercase == 'scissors' and computer_move == 'paper')
    ):
        outcome.append(PLAYER)
        # current_winner.append('Player')
        
    else:
        outcome.append(COMPUTER)
        # current_winner.append('Computer')
        
def current_winner(outcome):
    win = outcome[-1]
    if win == PLAYER:
        return 'Player'
    elif win == COMPUTER:
        return 'Computer'
    else:
        return 'Its a tie'


def main(outcome, current_winner):
    running = True
    while running:

        player_move = input('Choose Rock Paper or Scissors: ')
        player_move_lowercase = player_move.casefold()

        if player_move_lowercase not in['rock', 'paper', 'scissors']:
            print('Invalid input. Input must be Rock, Paper, Scissors')
        else:
            computer_move = random.choice(['rock', 'paper', 'scissors'])

            winning_move(player_move_lowercase, computer_move)
        
            print(f'Computers move is: {computer_move}, The winner of this round is: {current_winner(outcome)}')

        if winner(outcome):
            running = False


if __name__ == "__main__":
    main(outcome, current_winner)

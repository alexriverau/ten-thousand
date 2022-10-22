import game_logic

game = game_logic.GameLogic()
round = 1
playing = True


def take_turn():
    print('Rolling 6 dice...')
    roll = game.roll_dice(6)
    dice_printout = '*** '
    for die in roll:
        dice_printout += str(die) + ' '
    dice_printout += '***'
    return dice_printout


def bank():
    print('Enter dice to keep, or (q)uit:')
    response = input('> ')
    if response == 'q' or response == 'quit':
        print('Thanks for playing. You earned 0 points')
        global playing
        playing = False


def announce_round(round):
    print(f'Starting round {round}')


print('Welcome to Ten Thousand')
print(f'(y)es to play or (n)o to decline')

response = input('> ')

if response.lower() == 'n' or response.lower() == 'no':
    print('OK. Maybe another time')
    playing = False

if response.lower() == 'y' or response.lower() == 'yes':
    while playing:
        announce_round(round)
        print(take_turn())
        bank()




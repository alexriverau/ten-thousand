import game_logic

game = game_logic.GameLogic()
round = 1
playing = True
total_score = 0
kept_dice = []
num = 6


def take_turn(num):
    print(f'Rolling {num} dice...')
    roll = game.roll_dice(num)
    dice_printout = '*** '
    for die in roll:
        dice_printout += str(die) + ' '
    dice_printout += '***'
    return dice_printout


def bank():
    global total_score
    global round
    global num
    global kept_dice

    print('Enter dice to keep, or (q)uit:')
    response = input('> ')
    if response == 'q' or response == 'quit':
        print(f'Thanks for playing. You earned {total_score} points')
        global playing
        playing = False

    else:
        # Convert user input string into list of integers
        dice = []
        for die in response:
            dice.append(int(die))
            kept_dice.append(int(die))

        # Updates number of dice to re-roll
        num = 6 - len(kept_dice)

        # Calculate current number of points
        points = game.calculate_score(dice)
        print(f'You have {points} unbanked points and {6 - len(dice)} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')

        action = input('> ')

        # Bank
        if action == 'b' or action == 'bank':
            total_score += points
            print(f'You banked {points} points in round {round}')
            print(f'Total score is {total_score} points')
            round += 1

        # Roll
        if action == 'r' or action == 'roll':
            round += 1
            return

        # Quit
        if response == 'q' or response == 'quit':
            print(f'Thanks for playing. You earned {total_score} points')
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
        print(take_turn(6))
        bank()






import sys
from ten_thousand import game_logic
from ten_thousand import banker
#import game_logic
#import banker


class Game:

    game = game_logic.GameLogic()
    bank = banker.Banker()
    round_num = 1
    playing = True
    total_score = 0
    kept_dice = []
    number_of_dice = 6

    @staticmethod
    def want_to_play():
        print('Welcome to Ten Thousand')
        print(f'(y)es to play or (n)o to decline')
        response = input('> ')

        while response.lower() != 'y' and response.lower() != 'yes' and response.lower() != 'n' and response.lower() != 'no':
            print(f'(y)es to play or (n)o to decline')
            response = input('> ')

        if response.lower() == 'y' or response.lower() == 'yes':
            return True
        else:
            print('OK. Maybe another time')
            return False

    @staticmethod
    def print_roll(roll):
        dice_printout = '*** '
        for die in roll:
            dice_printout += str(die) + ' '
        dice_printout += '***'
        print(dice_printout)

    @staticmethod
    def rolling():
        # Calculate number of dice to roll
        num = Game.number_of_dice - len(Game.kept_dice)
        print(f'Rolling {num} dice...')

        # Roll dice, print, return roll
        roll = Game.game.roll_dice(num)
        Game.print_roll(roll)
        return roll

    @staticmethod
    def validate_keepers(roll, keepers):
        values = {}
        for die in roll:
            values.setdefault(str(die), 0)
            values[str(die)] += 1
        for num in keepers:
            if str(num) not in values or values[str(num)] == 0:
                return False
            values[str(num)] -= 1
        return True

    @staticmethod
    def get_player_selection(roll):
        print('Enter dice to keep, or (q)uit:')
        selection = input('> ')
        if selection.lower() == 'q' or selection.lower() == 'quit':
            return selection

        selection = [int(char) for char in selection]
        selection = tuple(selection)

        while not Game.validate_keepers(roll, selection):
            print('Cheater!!! Or possibly made a typo...')
            Game.print_roll(roll)
            selection = input('> ')
            if selection.lower() == 'q' or selection.lower() == 'quit':
                break
            selection = [int(char) for char in selection]
            selection = tuple(selection)
        return selection

    @staticmethod
    def quit(msg):
        Game.playing = False
        sys.exit(msg)

    @staticmethod
    def save_player_dice(selection):
        # Covert user input string into list of integers and save
        dice = [int(die) for die in selection]
        Game.kept_dice.extend(dice)
        return dice

    @staticmethod
    def get_player_action():
        print('(r)oll again, (b)ank your points or (q)uit: ')
        action = input('> ')
        while action.lower() != 'r' and action.lower() != 'roll' and action.lower() != 'b' and action.lower() != 'bank' and action.lower() != 'q' and action.lower() != 'quit':
            print('(r)oll again, (b)ank your points or (q)uit: ')
            action = input('> ')
        return action

    @staticmethod
    def run_turn():
        roll = Game.rolling()
        selection = Game.get_player_selection(roll)

        if selection == 'q' or selection == 'quit':
            Game.quit(f'Thanks for playing. You earned {Game.bank.balance} points')
            return

        dice = Game.save_player_dice(selection)
        points = Game.game.calculate_score(dice)
        print(f'You have {points} unbanked points and {Game.number_of_dice - len(Game.kept_dice)} dice remaining')

        action = Game.get_player_action()

        # Bank
        if action == 'b' or action == 'bank':
            Game.bank.shelved = Game.game.calculate_score(Game.kept_dice)
            banked_points = Game.bank.bank()
            print(f'You banked {banked_points} points in round {Game.round_num}')
            print(f'Total score is {Game.bank.balance} points')
            Game.round_num += 1
            Game.kept_dice = []
            return

        # Roll
        if action == 'r' or action == 'roll':
            Game.run_turn()
            return

        # Quit
        if action == 'q' or action == 'quit':
            Game.quit(f'Thanks for playing. You earned {Game.bank.balance} points')
            return

    @staticmethod
    def announce_round():
        print(f'Starting round {Game.round_num}')


def main():
    Game.playing = Game.want_to_play()
    while Game.playing:
        Game.announce_round()
        Game.run_turn()


if __name__ == '__main__':
    main()







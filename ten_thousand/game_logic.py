from collections import Counter


class GameLogic:
    pass

    @staticmethod
    def roll_dice(dice):
        import random
        # dice_list = [1, 2, 3, 4, 5, 6]
        # return_tuple = tuple(random.choice(dice_list))
        number_list = []
        for num in range(dice):
            roll = random.randint(1, 6)
            number_list.append(roll)
        number_list = tuple(number_list)
        return number_list

    @staticmethod
    def calculate_score(roll):
        score = 0
        counts = Counter(roll).most_common()

        for die in counts:
            if die[1] >= 3:
                if die[0] == 1:
                    score += die[0] * 1000 * (die[1] - 2)
                else:
                    score += die[0] * 100 * (die[1] - 2)
            else:
                if die[0] == 5:
                    score += 50*die[1]
                if die[0] == 1:
                    score += 100*die[1]
        return score



if __name__ == '__main__':
    print('ran directly as a module')
#     # to execute run: python -m ten_thousand.game_logic
#     # Executing without the -m "can" have a different import structure in certain aspects when doing multiple imports
#     # from different folders
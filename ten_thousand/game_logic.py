from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(dice):
        import random
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
            if len(counts) == 6:
                score = 1500
                break
            if len(counts) == 3:
                for pair in counts:
                    if pair[1] != 2:
                        break
                    score = 1500
            if die[1] >= 3:
                if die[0] == 1:
                    score += die[0] * 1000 * (die[1] - 2)
                else:
                    score += die[0] * 100 * (die[1] - 2)
            else:
                if die[0] == 5:
                    score += 50 * die[1]
                if die[0] == 1:
                    score += 100 * die[1]
        return score

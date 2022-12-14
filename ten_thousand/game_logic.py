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

        # Check for straight
        if len(counts) == 6:
            return 1500

        # Check for 3 pairs
        if len(counts) == 3:
            pair_count = 0
            for pair in counts:
                if pair[1] == 2:
                    pair_count += 1
            if pair_count == 3:
                return 1500

        for die in counts:
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

    @staticmethod
    def get_scorers(roll):
        roll = list(roll)
        max_score = GameLogic.calculate_score(roll)

        scorers = []

        for idx, die in enumerate(roll):
            del roll[idx]
            score = GameLogic.calculate_score(roll)
            if score < max_score:
                scorers.append(die)
            roll.insert(idx, die)

        return tuple(scorers)

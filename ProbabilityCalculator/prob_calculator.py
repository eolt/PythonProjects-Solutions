import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **types):
        self.contents = []
        for typ in types.items():
            for i in range(typ[1]):
                self.contents.append(typ[0])

    def draw(self, num):
        if(num >= len(self.contents)):
            return self.contents

        drawn = []
        for picks in range(num):
            i = random.randrange(len(self.contents))
            drawn.append(self.contents[i])
            self.contents = self.contents[0:i] + self.contents[i+1:]

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    wins = 0

    for rounds in range(num_experiments):
        example = copy.copy(hat)
        drawn = example.draw(num_balls_drawn)

        correct = True
        for i in expected_balls:
            if(expected_balls[i] > drawn.count(i)):
                correct = False
                break

        if correct:
            wins += 1

    return wins / num_experiments

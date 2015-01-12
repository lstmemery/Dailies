from __future__ import unicode_literals
import random


class MathDice(object):

    def __init__(self, goal, dice):
        self.goal = random.randint(1, int(goal))
        self.dice = sorted([random.randint(1, 6) for _ in range(dice)], reverse=True)
        assert self.goal < sum(self.dice), 'Goal is larger than sum of all math dice!'
        self.positive, self.negative = self.dice[:], []

    def quick_add(self):
        if self.goal == sum(self.positive):
            return self.positive
        if (self.goal - sum(self.positive)) % 2 == 0 and (self.goal - sum(self.positive) > 0):
            for die in self.positive:
                pass

    def __str__(self):
        pass




if __name__ == '__main__':
    example = MathDice(12, 5)
    print example.goal
    print example.dice

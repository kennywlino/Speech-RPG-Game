import random

minimal_pairs = []
pronunciation_problems = []
tongue_twisters = []

def text_to_list():
    with open("minimal_pairs.txt") as file:
        for line in file:
            line = line.strip()
            minimal_pairs.append(line)
    with open("pronunciation_problems.txt") as file:
            for line in file:
                line = line.strip()
                pronunciation_problems.append(line)
    with open("tongue_twisters.txt") as file:
        for line in file:
            line = line.strip()
            tongue_twisters.append(line)

text_to_list()

class Enemy():
    def __init__(self, name, hp, damage, sentence):
        self.name = name
        self.sentence = sentence
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class EvilTwins(Enemy):
    def __init__(self):
        super().__init__(name="Evil Twins", hp=10, damage=5, sentence=random.choice(minimal_pairs))

class PP(Enemy):
    def __init__(self):
        super().__init__(name="Twisted Trees", hp=10, damage=10, sentence=random.choice(pronunciation_problems))

class Boss(Enemy):
    def __init__(self):
        super().__init__(name="Final Boss", hp=10, damage=15, sentence=random.choice(tongue_twisters))

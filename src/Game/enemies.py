import random
import _pickle as cPickle
import mini_pairs

# minimal_pairs = [] used only in ver 1 for list of minimal pair sentences
pronunciation_problems = []
tongue_twisters = []

def text_to_list():
    # used only in ver 1 for list of minimal pair sentences
    # with open("minimal_pairs.txt") as file:
    #     for line in file:
    #         line = line.strip()
    #         minimal_pairs.append(line)
    with open("pronunciation_problems.txt") as file:
            for line in file:
                line = line.strip()
                pronunciation_problems.append(line)
    with open("tongue_twisters.txt") as file:
        for line in file:
            line = line.strip()
            tongue_twisters.append(line)

text_to_list()

# the following are used for Evil Twins
with open("word_sent_dict.txt", "rb") as dictFile:
 	word_sent_dict = cPickle.load(dictFile)
with open("min_pair_list.txt", "rb") as listFile:
	mp_list = cPickle.load(listFile)

# gets minimal pair sentences for Evil Twins
def get_mp_sentences():
    min_pair = mini_pairs.get_min_pair(mp_list)
    while ((min_pair[0] not in word_sent_dict) or (min_pair[1] not in word_sent_dict)):
    	min_pair = mini_pairs.get_min_pair(mp_list)
    random_sents = mini_pairs.random_sentences(min_pair, word_sent_dict) # returns a dictionary of mp words to rand sents
    return (random_sents)

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
        super().__init__(name="Evil Twins", hp=10, damage=5, sentence=get_mp_sentences())

class PP(Enemy):
    def __init__(self):
        super().__init__(name="Twisted Trees", hp=10, damage=10, sentence=random.choice(pronunciation_problems))

class Boss(Enemy):
    def __init__(self):
        super().__init__(name="Final Boss", hp=10, damage=15, sentence=random.choice(tongue_twisters))

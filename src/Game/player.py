'''
Class Player defines the default settings and functions of a user playing the game.
Features such as inventories are currently defined but are not used in the current version
of the game.
'''

import items, world, speech, feedback, minimal_pairs_advice
import random
import mini_pairs
import _pickle as cPickle

class Player():
    def __init__(self):
        self.inventory = [] # not currently being used
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.user_text=''

    def is_alive(self):
        return self.hp > 0

    # not being used in this version
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    # this is the module that requires checking the speech to text to the enemies sentences
    def attack(self, enemy):
        # if enemy is evil twins, print both sentences but say only one
        if enemy.name == "Evil Twins":
            test_sent = self.evil_twins_attack(enemy)
        else:
            test_sent = enemy.sentence
            print(test_sent + '\n')
        self.user_text = (speech.recognize_speech(enemy)).lower()
        if self.user_text == test_sent.lower():
            damage = enemy.hp
            enemy.hp -= damage
            print("You killed {}!".format(enemy.name))
        else:
            self.hp -= enemy.damage
            self.feedback(enemy, test_sent)

    # a special method to define the new Evil Twins sentences
    def evil_twins_attack(self, enemy):
        with open("associations.txt", "rb") as dictFile:
            associations = cPickle.load(dictFile)
        class bcolors:
        	OKGREEN = '\033[92m'
        	ENDC = '\033[0m'
        ref_and_test_word = mini_pairs.get_test_word(enemy.sentence)
        test_word = ref_and_test_word[1]
        ref_word = ref_and_test_word[0]
        ref_sent = enemy.sentence[ref_word]
        test_sent = enemy.sentence[test_word]
        word_info = associations[test_word]
        print("In the first sentence, the word in green should help you guess "
        "the missing word in the next one. Clue: they are almost twins! \n")
        ref_sent_split = ref_sent.split(' ')
        #print(words1)
        counter = 0
        for i, word in enumerate(ref_sent_split):
        	if word == ref_word:
        		print("1. " + ' '.join(ref_sent_split[:i]) + " " +
        		str(bcolors.OKGREEN + ref_word + bcolors.ENDC) + ' '
        		+ ' '.join(ref_sent_split[i+1:])+ "\n\n")
        print("2.",test_sent.replace(test_word, '________'))
        print("\n\t- Word definition: ", word_info[2])
        print("\n\t- Synonyms: ", end = " ")
        if not word_info[0]:
        	print('n/a')
        else:
        	print (', '.join(word_info[0]))
        print("\n\t- Antonyms: ", end = " ")
        if not word_info[1]:
        	print('n/a')
        else:
        	print(', '.join(word_info[1]),"\n\n")
        return (test_sent)


    # returns feedback in ARPAbet, IPA, or descriptive format (mouth positioning)
    # depending on user input
    def feedback(self, enemy, sentence):
        print("Enemy does {} damage. You have {} HP remaining.".format(enemy.damage, self.hp))
        option=input("Oops, looks like you need to improve your communication skills. The fairies of the forest come in your help. 'Hello wanderer! You have 3 different ways to get feedback. Choose an option so we can perform our magic!'\n1. Get the arpabet transcription\n2. Get the IPA transcription\n3. Get some descriptive advice\n4. Get the pronunciation of the sentence\n\n")
        while option not in '1234':
            option=input("Try again with 1, 2, 3, or 4 please.\n\n")
        if option == "1":
            print(feedback.arpabet(sentence.rstrip('.')))
        elif option == "2":
            print(feedback.ipa(sentence))
        elif option == "3":
            ipa_sentence = feedback.ipa(sentence)
            #feedback.minimal_pairs_advice(self.user_text,enemy.sentence, ipa_sentence)
            minimal_pairs_advice.minimal_pairs_advice(self.user_text,sentence,ipa_sentence)
        elif option == "4":
            text_to_speech=feedback.tts(sentence)
        # elif option == "5":

        # option to pass up on feedback

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

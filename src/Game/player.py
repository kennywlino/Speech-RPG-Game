'''
Class Player defines the default settings and functions of a user playing the game.
Features such as inventories are currently defined but are not used in the current version
of the game.
'''

import items, world, speech, feedback
import random

class Player():
    def __init__(self):
        self.inventory = [] # not currently being used
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

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
        print(enemy.sentence + '\n')
        user_text = (speech.recognize_speech()).lower()
        if user_text == enemy.sentence.lower():
            damage = enemy.hp
            enemy.hp -= damage
            print("You killed {}!".format(enemy.name))
        else:
            self.hp -= enemy.damage
            feedback()

    # returns feedback in ARPAbet, IPA, or descriptive format (mouth positioning)
    # depending on user input
    def feedback():
        print("Enemy does {} damage. You have {} HP remaining.".format(enemy.damage, self.hp))
        option=input("Oops, looks like you need to improve your communication skills. The fairies of the forest come in your help. 'Hello wanderer! You have 3 different ways to get feedback. Choose an option so we can perform our magic!'\n1. Get the arpabet transcription\n2. Get the IPA transcription\n3. Get some descriptive advice\n\n")
        while option not in '1234':
            option=input("Try again with 1, 2, or 3 please.\n\n")
        if option == "1":
            print(feedback.arpabet(enemy.sentence.rstrip('.')))
        elif option == "2":
            print(feedback.ipa(enemy.sentence))
        elif option == "3":
            ipa_sentence = feedback.ipa(enemy.sentence)
            feedback.minimal_pairs_advice(enemy.sentence, ipa_sentence)
        elif option == "4":
            # option to pass up on feedback

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

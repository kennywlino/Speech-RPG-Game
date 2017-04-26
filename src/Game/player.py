'''
Class Player defines the default settings and functions of a user playing the game.
Features such as inventories are currently defined but are not used in the current version
of the game.
'''

import items, world, speech
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
    # Make the change to the player that they lose HP if they say the sentence wrong HERE
    def attack(self, enemy):
        user_text = speech.recognize_speech()
        if user_text == # what the enemies sentence is
            damage = random.randint(3, enemy.hp - 1)
            if damage == enemy.hp:
                print("WOAH! That was critical!")
            enemy.hp -= damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.",format(enemy.name, enemy.hp))
            
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
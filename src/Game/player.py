from Game import items, enemies, actions, world
import random

class Player():
    def __init__(self):
        self.inventory = []
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
    
    def is_alive(self):
        return self.hp > 0
    
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
        
    def attack(self, enemy):
        attack = random.randint(1, enemy.hp)
        if attack == enemy.hp:
            print("WOAH! That was critical!")
        enemy.hp -= attack
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.",format(enemy.name, enemy.hp))
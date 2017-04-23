'''
Class MapTile defines the layout of tile space within the world of the game.
Taken from: http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-2-the-world-space/
'''

from Game import items
from Game.enemies import Enemy

class MapTile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    
def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()

class StartingRoom(MapTile):
    # PLACEHOLDER FOR INTRO TEXT; CHANGE LATER
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
    
    def modify_player(self, player):
        #Room has no action on player
        pass

class EnemyRoom(MapTile):
    def __init(self, x, y, enemy):
        self.enemy = Enemy
        super().__init__(x, y)
    
    def intro_text(self):
        return """
        Watch out! You've encountered an enemy!
        """
    
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
            
 
class EmptyWoodsPath(MapTile):
    def intro_text(self):
        return """
        A seemingly quiet part of the woods. Are we out of the woods yet...
        """
    
    def modify_player(self, player):
        # Room has no action on player
        pass
    
class ExitRoom(MapTile):
    def intro_text(self):
        return """
        You luckily made your way out of the woods. You're safe for now... until next time...
        """
    
    def modify_player(self, the_player):
        the_player.victory = True
        

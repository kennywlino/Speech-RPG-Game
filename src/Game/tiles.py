'''
Class MapTile defines the layout of tile space within the world of the game.
Taken from: http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-2-the-world-space/
'''

from Game import items

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


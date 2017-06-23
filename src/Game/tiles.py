'''
Class MapTile defines the layout of tile space within the world of the game.
Taken from: http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-2-the-world-space/
'''

import items, enemies, actions, world

# one tile (e.g. room) on the map based on its (x,y) coordinates
class MapTile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    # defines the introductory text when the user enters the room
    def intro_text(self):
        raise NotImplementedError() # raises error as no room should be of type "MapTile"
    
    def modify_player(self, player):
        raise NotImplementedError() # raises error as no room should be of type "MapTile"
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        return moves

# defines the room that the user begins the game in
class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You wake up in the middle of a forest. You see four different paths,
        each looking equally gloomy.
        """
        
    def modify_player(self, player):
        #Room has no action on player
        pass
    
# defines a simple room where the user does not encounter an emeny
class EmptyWoodsPath(MapTile):
    def intro_text(self):
        return """
        A seemingly quiet part of the woods. Are we out of the woods yet...
        """
    
    def modify_player(self, player):
        # Room has no action on player
        pass

# defines the basic enemy room where the user will have to 'fight' 
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
                
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()
    
    def modify_player(self, player):
        # Room has no action on player
        pass

# A room that contains enemies that use words with minimal pairs.     
class EvilTwinsRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.EvilTwins())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Two eerily looking twins randomly pop out of the woods. They say to you in unison:
            "We know what you're thinking. WE'RE NOT TWINS!"
            """
        else:
            return """
            Looks like you've already defeated this enemy. Lucky you.
            """

class PPRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.PP())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Suddenly the trees in the distance come together to form a wall,
            blocking your path. They open their eyes and say, "To pass us,
            and to continue on your path, you need to win against us or face our wrath!"
            """
        else:
            return """
            Looks like the trees are back to sleep.
            """
            
class BossRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Boss())
    
    def intro_text(self):
        return """
        WOOOOOOOO you've made it... wait.
        *thump* You encounter an old, grumpy troll.
        He(?) says to you, "LOL you thought you were about to just walk out of here,
        but before you go, I need you to spit a rap!" 
        """

# defines the final room that allows the user to 'escape' and win the game
class ExitRoom(MapTile):
    def intro_text(self):
        return """
        You luckily made your way out of the woods. You're safe for now... until next time...
        """
    
    def modify_player(self, player):
        player.victory = True
        

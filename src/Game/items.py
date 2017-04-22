'''
The Item class defines basic information about any items found within the game
Taken from: http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/
'''

class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description= "A coin with {} value.".format(str(self.amt)),
                         value= self.amt)
        
class Tool(Item):
    def __init__(self, name, description, value, usage):
        self.usage = usage
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, 
                                                             self.value, self.usage)

class Key(Tool):
    def __init__(self):
        super().__init__(name="Key",
                         description="A small key, perhaps used to open a door?",
                         value=0,
                         usage='door')
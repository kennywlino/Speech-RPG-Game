class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp
        self.damage = damage
    
    def is_alive(self):
        return self.hp > 0
    
class TongueTwister(Enemy):
    def __init__(self):
        super().__init__(name="Tongue Twister", hp=10, damage=5)

class Riddle(Enemy):
    def __init__(self):
        super().__init__(name="Riddle", hp=20, damage=10)
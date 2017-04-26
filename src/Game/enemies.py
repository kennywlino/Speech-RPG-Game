class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp
        self.damage = damage
    
    def is_alive(self):
        return self.hp > 0
    
    
class EvilTwins(Enemy):
    def __init__(self):
        super().__init__(name="Evil Twins", hp=10, damage=5)

class PP(Enemy):
    def __init__(self):
        super().__init__(name="PP", hp=20, damage=10)
        
class Boss(Enemy):
    def __init__(self):
        super().__init__(name="Final Boss", hp=30, damage=15)
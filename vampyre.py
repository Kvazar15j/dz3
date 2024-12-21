from Character import Character

class Vampyre(Character):
    vampirism =  0.1

    def __init__(self, name, health=100, damage=5, defence=0, vampirism = 0.1):
        Character.__init__(self, name, health, damage, defence)
        self.vampirism = vampirism

    def attack(self, target):
        vamp = self.damage * self.vampirism
        self.health = (self.health + vamp)
        return target.take_damage(self.damage)
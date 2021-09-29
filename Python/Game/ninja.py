class Ninja:

    def __init__( self , name, strength = 10, speed = 5, health = 100 ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
    
    def show_stats( self ):
        if self.health > 0:
            print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        else: print (f"{self.name} is super dead!")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

    def heal (self):
        self.health += 10
        if(self.health > 100):
            self.health = 100
        return self

    def power(self):
        if self.health >= 33:
            self.strength += 5
        else:
            self.strength += 10
        return self 

    def longrange(self, pirate):
        if(self.speed > pirate.speed):
            pirate.health -= (self.strength*.5)
        return self
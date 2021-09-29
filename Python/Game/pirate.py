class Pirate:

    def __init__( self , name,strength = 15,speed = 3,health = 10):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health    

    def show_stats( self ):
        if self.health > 0:
            print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        else: print (f"{self.name} is super dead!")
        return self 

    def attack ( self , ninja ):
        ninja.health -= self.strength
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

    def longrange(self, ninja):
        if(self.speed > ninja.speed):
            ninja.health -= (self.strength*.5)
        return self 
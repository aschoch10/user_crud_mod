import ninja
import pirate

from ninja import Ninja
from pirate import Pirate

michelangelo = Ninja("Michelangelo")
jack_sparrow = Pirate("Jack Sparrow")
leonardo = Ninja("Leonardo")
black_beard = Pirate("Black Beard")

characters = {"Michelangelo": michelangelo,"Jack Sparrow": jack_sparrow, "Black Beard": black_beard, "Leonardo": leonardo}
skills = {"Attack":"Attack" , "Heal": "Heal", "Power": "Power", "Longrange": "Longrange"}

print("Welcome to Ninjas vs. Pirates!")
jack_sparrow.show_stats()
michelangelo.show_stats()

print("Ninjas: Michelangelo, Leonardo\nPirates: Jack Sparrow, Black Beard")
playerchoice = input("Choose Your Ninja Character: ")

while playerchoice not in characters:
    print("Invalid Player Choice.")
    playerchoice = input("Choose Your Ninja Character: ")
ninjaUser = characters[playerchoice]


print("Ninjas: Michelangelo, Leonardo\nPirates: Jack Sparrow, Black Beard")
playerchoice = input("Choose Your Pirate Character: ")

while playerchoice not in characters:
    print("Invalid Player Choice.")
    playerchoice = input("Choose Your Pirate Character: ")
pirateUser = characters[playerchoice]

print(f"You have chosen ninja:{ninjaUser.__dict__}, pirate:{pirateUser.__dict__}")

user = ninjaUser

while ninjaUser.health > 0 or pirateUser.health > 0:
    if ninjaUser.health <= 0 or pirateUser.health <= 0:
        print(f"{'GAME OVER':-^50}")  
        break
    print(f"Now it's {user.name}'s turn.")

    if user == ninjaUser:
        print(f"{user.name} please choose skill: Attack  Heal  Power  Longrange")
        skill = input("Which skills would you like to use?: ")
        # choose skill here
        while skill not in skills:
            print("Invalid Choice, please choose again.")
            skill = input("Which skills would you like to use?: ")
        if skill == skills["Attack"]:
            ninjaUser.attack(pirateUser)
            print(f"{ninjaUser.name} attacked Jack Sparrow!")
        elif skill == skills["Heal"]:
            ninjaUser.heal()
            print(f'{ninjaUser.name} has healed himself!')
        elif skill == skills["Power"]:
            ninjaUser.power()
            print(f"{ninjaUser.name} powered up!")
        elif skill == skills["Longrange"]:
            ninjaUser.longrange(pirateUser)
            print(f"{ninjaUser.name} used long range attack!")
        user = pirateUser
        pirateUser.show_stats()
        ninjaUser.show_stats()


    elif user == pirateUser:
            print(f"{user.name} please choose skill: Attack  Heal  Power  Longrange")
            skill = input("Which skills would you like to use?: ")
            # choose skill here
            while skill not in skills:
                print("Invalid Choice, please choose again.")
                skill = input("Which skills would you like to use?: ")
            if skill == skills["Attack"]:
                pirateUser.attack(ninjaUser)
                print(f"{pirateUser.name} attacked Michelangelo!")
            elif skill == skills["Heal"]:
                pirateUser.heal()
                print(f'{pirateUser.name} has healed himself!')
            elif skill == skills["Power"]:
                pirateUser.power()
                print(f"{pirateUser.name} powered up!")
            elif skill == skills["Longrange"]:
                pirateUser.longrange(ninjaUser)
                print(f"{pirateUser.name} used long range attack!")
            user = ninjaUser
            pirateUser.show_stats()
            ninjaUser.show_stats()



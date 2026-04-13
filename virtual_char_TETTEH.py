# Virtual Character Simulator
# DANIEL TETTEH
# CMSC 150 - SECTION 2
# MARCH 20

class Food:
    '''Food for the virtual character to eat'''
    def __init__(self,name:str,pts:int = 2):
        self.name = name
        self.pts = 2

    def get_name(self):
        return self.name

    def get_pts(self):
        return self.pts
        

class Toy:
    '''Toy for the virtual character to play with'''
    def __init__(self,name:str):
        self.name = name

    def get_name(self):
        return self.name
        


class VirtualChar:
    def __init__(self,name:str,char_type:str):
        '''Initializer function for the virtual character class'''
        self.name = name
        self.char_type = char_type
        
        self.hunger = 5
        self.max_hunger = 10
        self.mood = "neutral"

        self.moodSwing()


    def stats(self):
        '''Prints all of the properties of the virtual character'''
        print(f"Name: {self.name}")
        print(f"Type: {self.char_type}")
        print(f"Hunger: {self.hunger} / {self.max_hunger}")
        print(f"Mood: {self.mood}")


    def eat(self,char_food:Food):
        '''The character eats food to restore hunger'''

        self.hunger += char_food.get_pts()

        if self.hunger > 10:
            self.hunger = 10

        print(f"{self.name} ate {char_food.get_name()}. Restored {self.hunger} hunger!")

        self.moodSwing()
        
    def play(self,char_toy:Toy):
        '''The character plays with a toy to restore mood, but loses hunger'''
        print(f"{self.name} used a {char_toy.get_name()}")

        self.hunger -= 1

        if self.hunger < 0:
            self.hunger = 0

        self.moodSwing()

    def moodSwing(self):
        '''Changes the character's mood based on their hunger level'''

        x = self.max_hunger / 2
        y = self.max_hunger / 4

        if self.hunger > x:
            self.mood = "happy"
                
        elif x >= self.hunger > y:
            self.mood = "neutral"
                
        elif y >= self.hunger:
            self.mood = "sad"


def main():
    m = VirtualChar("Max", "Dog")
    r = VirtualChar("Ruby", "Cat")
    c = VirtualChar("Coco", "Dog")
    m.stats()
    print("")
    r.stats()
    print("")
    c.stats()
    

    f = Toy("fidget toy")

    m.play(f)

    g = Food("puppy chow")

    m.eat(g)

if __name__ == "__main__":
    main()


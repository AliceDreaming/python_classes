class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        #TODO
        # Forgive me I really have no idea how to describe drum sound in English
        super().__init__(["Dong", "Tong", "Ting", "Hehe"])
    
    #TODO
    def solo(self):
        # call the solo in parent class with default value 4
        super().solo(4)
        
class Band(object):
    def __init__(self):
        self.musicians=[]
    
    def hire_musician(musician):
        self.musicians.append(musician)
        
    def fire_musician(musician):
        self.musicians.pop()
    
    #TODO:I don't quite understand how this works for a band
    def play_solo():
        for musician in self.musicians:
            musician.solo(4)
  
if(__name__ == '__main__')         
    david = Guitarist()
    derek= Bassist()
    jorge = Drummer()
    
    popBand = Band()
    popBand.hire_musician(david)
    popBand.hire_musician(derek)
    popBand.hire_musician(jorge)
    popBand.play_solo()

    popBand.fire_musician()
    popBand.play_solo()



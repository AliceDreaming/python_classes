class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])

# The Musician class is the parent of the Bassist class        
class Bassist(Musician): 
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        #TODO
        # Forgive me I really have no idea how to describe drum sound in English
        super(Drummer, self).__init__(["Dong", "Tong", "Ting", "Hehe"])
        
    def __count__(self):
        for i in range(4):
            print i
        
class Band(object):
    def __init__(self):
        self.musicians=[]
    
    def hire_musician(self, musician):
        self.musicians.append(musician)
        
    def fire_musician(self, musician):
        self.musicians.remove(musician)
    
    def play_solo(self, length):
        for musician in self.musicians:
            musician.solo(length)
  
if(__name__ == '__main__'):         
    david = Guitarist()
    derek= Bassist()
    jorge = Drummer()
    
    popBand = Band()
    popBand.hire_musician(david)
    popBand.hire_musician(derek)
    popBand.hire_musician(jorge)
    jorge.__count__()
    length = 10
    popBand.play_solo(length)

    popBand.fire_musician(david)
    popBand.play_solo(length)



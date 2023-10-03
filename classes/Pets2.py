class Pet:
    def __init__(self,n,a,h,p):
       self.name = n
       self.age = a
       self.hunger = h
       self.playful = p

    #getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    #setters
    def setName(self,xname):
        self.name = xname

    def setAge(self,age):
        self.age = age

    def setHunger(self,hunger):
        self.hunger = hunger

    def setPlayful(self,playful):
        self.playful = playful

    def __str__(self) -> str:
        return(self.name + " is " + str(self.age) + " years old")

class Dog(Pet):
    def __init__(self,name,age,hunger,playful,breed,favouriteToy):
        Pet.__init__(self,name,age,hunger,playful)
        self.breed = breed
        self.FavouriteToy = favouriteToy

    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " + self.FavouriteToy)
        else:
            return ("Dog doesnt want to play")

class Cat(Pet):
    def __init__(self, n, a, h, p,place):
        Pet.__init__(self,n, a, h, p)
        self.FavouritePlaceToSit = place

    def wantsToSit(self):
        if self.playful == False:
            print("The cat wants to sit in",self.FavouritePlaceToSit)
        else:
            print("The cat wants to play")

    def __str__(self):
        return(self.name + " likes to sit in the " + self.FavouritePlaceToSit)

class Human():

    def __init__(self,name,Pets):
        self.name = name
        self.pets = Pets

    def hasPets(self):
        if len(self.pets) != 0:
            return "Yes"
        else:
            return "No"
        

huskyDog = Dog("Snowball",3,False,True,"Husky","Stick")

Play = huskyDog.wantsToPlay()

print(Play)

huskyDog.playful = False

Play = huskyDog.wantsToPlay()

print(Play)

typicalCat = Cat("fluffy",3,False,False,"in the sun ray")
typicalCat.wantsToSit()

print(typicalCat)

print(huskyDog)

averageHuman = Human("Alice",[huskyDog,typicalCat])

print(averageHuman.hasPets())
print(averageHuman.pets[0])
print(averageHuman.pets[0].name)
        
    
        


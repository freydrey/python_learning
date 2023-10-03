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

Pet1 = Pet("Jim",3,False,True)

print(Pet1.getName())
print(Pet1.getPlayful())
Pet1.setName("Snowball")
print(Pet1.getName())
print(Pet1.name)
Pet1.name = "Jim"
print(Pet1.getName)


        


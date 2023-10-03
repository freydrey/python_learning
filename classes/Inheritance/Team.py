class Team:
    def __init__(self, Name = "Name", Origin = "Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin
    
    def DefineTeamName(self,Name):
        self.TeamName = Name

    def DefineTeamOrigin(self,Origin):
        self.TeamOrigin = Origin


class Player(Team):
    def __init__(self,PlayerName,PPoints,TeamName,TeamOrigin):
        Team.__init__(self,TeamName,TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoints = PPoints

    def ScoredPoints(self):
        self.PlayerPoints += 1

    def setName(self,Name):
        self.PlayerName = Name    
    
    def __str__(self):
        return self.PlayerName + " has scored: " + self.PlayerPoints + " points"


Player1 = Player("Sid",0,"Sharks","Chicago")

print(Player1.PlayerName)
print(Player1.PlayerPoints)
print(Player1.TeamName)
print(Player1.TeamOrigin)

Player1.ScoredPoints()
print(Player1.PlayerPoints)

print(Player1)
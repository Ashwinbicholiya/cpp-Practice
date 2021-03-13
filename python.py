class Player:
    def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
        self.playername =playerName
        self.playerCountry = playerCountry
        self.playerAge = playerAge
        self.noOfRuns = noOfRuns
        self.noOfMatches = noOfMatches
        self.noOfWickets = noOfWickets

class Teams:
    def __init__(self,pass_list):
        self.playerlist = pass_list
    def getMinRuns(self):
        minRuns =[]
        for i in self.playerlist:
            for j in noOfRuns:
                minRuns.append(j)
        for i in self.playerlist:
            for j in noOfRuns:
                if j == min(minRuns):
                    return j
    def getMaxRuns(self):
        maxRuns = []
        for i in self.playerlist:
            for j in noOfRuns:
                maxRuns.append(j)
        for i in self.playerlist:
            for j in noOfRuns:
                if j == max(maxRuns):
                    return j

if __name__ =="__main__":
    n=int(input())
    pass_list=[]
    for i in range(n):
        playerName =input()
        playerCountry=input()
        playerAge=int(input())
        noOfMatches=int(input())
        noOfRuns=int(input())
        noOfWickets=int(input())
    
    o1=Teams(pass_list)
    print(o1.getMinRuns())
    print(o1.getMaxRuns())

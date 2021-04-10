class Player:
    def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
        self.playerName =playerName
        self.playerCountry = playerCountry
        self.playerAge = playerAge
        self.noOfRuns = noOfRuns
        self.noOfMatches = noOfMatches
        self.noOfWickets = noOfWickets

class Teams:
    def __init__(self,pass_list):
        self.playerlist = pass_list
    def getMinRuns(self):
        r =[]
        for i in self.playerlist:
            r.append(i.noOfRuns)
        min1=min(r)  
        result=[]
        for i in self.playerlist:
            if i.noOfRuns == min1:
                result.append(i.playerName)
                result.append(min1)
                result.append(i.playerCountry)
        return result
    def getMaxWickets(self):
        r=[]
        for i in self.playerlist:
            r.append(i.noOfWickets)
        max1=max(r)
        result = []
        for i in self.playerlist:
            if i.noOfWickets == max1:
                result.append(i.playerName)
                result.append(max1)
                result.append(i.playerCountry)
        return result
            

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
        pass_list.append(Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets))
    
    t=Teams(pass_list)
    r1=t.getMinRuns()
    r2=t.getMaxWickets()

    for i in range(len(r1)):
        print(r1[i])
    for i in range(len(r2)):
        print(r2[i])



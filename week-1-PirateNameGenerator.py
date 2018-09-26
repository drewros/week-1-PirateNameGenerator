import random

class PirateNameGenerator():
    origFirst = ""
    origLast = ""

    firstList = ["Fluffbucket", "Squidlips", "Scallywag", "Landlubber", "Sharkbait"]
    lastList = ["Chumbucket", "Swashbuckler", "McStinky", "Hornswaggler", "Barnacle"]

    def __init__(self, firstName, lastName):
        self.origFirst = firstName
        self.origLast = lastName

    def CreateName(self):
        x = random.randint(0, len(self.firstList)-1)
        y = random.randint(0, len(self.lastList)-1)
        return self.firstList[x] + self.lastList[y]


mypirate = PirateNameGenerator("Drew", "Rosenberg")

print (mypirate.origFirst, mypirate.origLast)
print (mypirate.CreateName())

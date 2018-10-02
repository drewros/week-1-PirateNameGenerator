import random
from tkinter import *

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

root = Tk()

#create the controls
myfont = "Arial 14"
#register the image
banner = PhotoImage(file="pirate-banner.gif")
#resize the image
#shrink
banner = banner.subsample(2,2)

title = Label(root, text="Determine Your Pirate Name", font="Arial 20 bold")
flabel = Label(root, text="First Name", font=myfont)
llabel = Label(root, text="Last Name", font=myfont)
ftext = Entry(root, font=myfont)
ltext = Entry(root, font=myfont)
bshow = Button(root, text="Show My Name", font=myfont)
output = Label(root, image=banner)

#add the controls to the window
title.grid(row=0, column=0, columnspan=2)
flabel.grid(row=1, column=0)
llabel.grid(row=2, column=0)
ftext.grid(row=1, column=1)
ltext.grid(row=2, column=1)
bshow.grid(row=3, column=0, columnspan=2)
output.grid(row=4, column=0, columnspan=2)

root.mainloop()

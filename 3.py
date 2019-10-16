def EggsIntoBoxs(NumberOfEggs):
    global NumberOfBoxes
    global EggsLeftOver
    NumberOfBoxes = int(NumberOfEggs)//6
    EggsLeftOver = int(NumberOfEggs)%6

EggsIntoBoxs(35)
print(NumberOfBoxes,EggsLeftOver)

#Exercise utilizing nested lists and input checking

def setMap():
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    return [row1, row2, row3]

def printInputError():
    print("Please enter valid coordinates.")
    print("## ColumnRow format [1-3][1-3] Example \"11\" would be top left.")

def getValidPosition():
    position = input("Where do you want to put the treasure? ")
    if(position[0].isnumeric() and position[1].isnumeric()):
        intPosition = []
        intPosition.append(int(position[0])) #python will not allow the reassignment of this value to an int
        intPosition.append(int(position[1])) 
        if(intPosition[0] > 3 or intPosition[0] < 1 or intPosition[1] > 3 or intPosition[1] < 1):
            printInputError()
            return getValidPosition()
        else:
            return intPosition
    else:
        printInputError()
        return getValidPosition()

def markMap(position, map):
    map[position[0]-1][position[1]-1] = "X"
    return map

def printMap(map):
    print(f"{map[0]}\n{map[1]}\n{map[2]}")

print("Time to hide the treasure on the grid! ColumnRow format. Example \"11\" would be top left.")
#Set an unmarked map
map = setMap()

#ask for the position from the user
position = getValidPosition()

map = markMap(position, map)

printMap(map)
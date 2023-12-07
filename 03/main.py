import re

schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

around = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,1],
    [1,1],
    [1,0],
    [1,-1],
    [0,-1]
]
schematic = open('input.txt').read()

def prepareSchematic(schem):
    """surround schematic with dots so I don't need to handle edge cases"""
    schemList = schem.strip().split('\n') #turn string into list
    dotString = '.' * len(schemList[0]) # create row of .s that is same width as schematic
    schemList = [dotString] + schemList[:] + [dotString]
    for i in range(len(schemList)):
        schemList[i] = '.' + schemList[i] + '.'
    return schemList

def findGearsInLine(schemLine):
    gearsList = []
    gearLoc = schemLine.find('*')
    startSlice = 0
    while gearLoc != -1:
        gearsList.append(gearLoc + startSlice)
        startSlice += gearLoc + 1
        gearLoc = schemLine[startSlice:].find('*')

    return gearsList

def getPartNumber(line, partIndex):
    print(line, "index",partIndex,'value', line[partIndex])
    indexOffset = 1
    nextChar = line[partIndex]
    numStr = ""
    #search left
    while nextChar.isdigit():
        numStr = nextChar + numStr
        nextChar = line[partIndex - indexOffset]
        indexOffset += 1
    indexOffset = 2

    nextChar = line[partIndex + 1]
    #search right
    while nextChar.isdigit():
        numStr = numStr + nextChar
        nextChar = line[partIndex + indexOffset]
        indexOffset += 1

    return int(numStr)


def findPartsAroundGear(schematicList, gearLocation):
    gearLine = gearLocation[0]
    gearIndex = gearLocation[1]
    lastGearLine = gearLine
    lastDigit = False
    numberLocations = []
    for i in around:
        aroundGearLine = i[0] + gearLine
        aroundGearIndex = i[1] + gearIndex
        foundDigit = schematicList[aroundGearLine][aroundGearIndex].isdigit()
        isNewNumber = (foundDigit != lastDigit or lastGearLine != aroundGearLine)
        if foundDigit and isNewNumber:
            numberLocations.append([aroundGearLine, aroundGearIndex])
        lastGearLine = aroundGearLine
        lastDigit = foundDigit
    
    if len(numberLocations) == 2:
        return numberLocations

    return []


def findPartPairs(schematic, gears):
    partPairs = []
    for gear in gears:
        partPair = findPartsAroundGear(schematic, gear)
        if partPair:
            partPairs.append(partPair)
    return partPairs


def findGears(schematic):
    gearsList = []
    for i in range(len(schematic)):
        gearsInLine = findGearsInLine(schematic[i])
        for gearIndex in gearsInLine:
            gearsList.append([i,gearIndex])

    return gearsList

def main():
    sum = 0
    schematicList = prepareSchematic(schematic)
    gears = findGears(schematicList)
    partPairs = findPartPairs(schematicList, gears)

    for pair in partPairs:
        gearRatio = 1
        for part in pair:
            partLine = schematicList[part[0]]
            partIndex = part[1]
            gearRatio = gearRatio * getPartNumber(partLine, partIndex)

        sum += gearRatio

    return sum

print(main())
# print([0,1] + [2,3])
test = ".........*.602.........571-.......................*...*.............199.....$.........181.......*......980....292............................."

# getPartNumber('.......755..', 7)
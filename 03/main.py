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
    [0,-1],
    [0,0],
    [0,1],
    [1,1],
    [2,1],
    [2,0],
    [2,-1],
    [1,-1]
]
# schematic = open('input.txt').read()

def prepareSchematic(schem):
    """surround schematic with dots so I don't need to handle edge cases"""
    schemList = schem.strip().split('\n') #turn string into list
    dotString = '.' * len(schemList[0]) # create row of .s that is same width as schematic
    schemList = [dotString] + schemList[:] + [dotString]
    for i in range(len(schemList)):
        schemList[i] = '.' + schemList[i] + '.'
    return schemList

def isPartNumber(numArea):
    for item in numArea:
        if len(re.sub('[0-9\.]', '', item)) > 0:
            return True
    return False

def findNumber(schematic, index):
    numberRange = []
    lineSum = 0
    numStr = ""
    lineStr = schematic[index]
    for i in range(len(lineStr)):
        if lineStr[i].isdigit():
            numStr += lineStr[i]
            if numberRange == []:
                numberRange.append(i-1)
        elif numStr != "":
            numberRange.append(i+1)
            numArea = [
                schematic[index-1][numberRange[0]:numberRange[1]],
                schematic[index][numberRange[0]:numberRange[1]],
                schematic[index+1][numberRange[0]:numberRange[1]]
            ]
            
            if isPartNumber(numArea):
                lineSum += int(numStr)
            numStr = ""
            numberRange = []

    return lineSum

def findGears(schemList, i):
    gearsList = []
    schemLine = schemList[i]
    gearLoc = schemLine.find('*')
    startSlice = 0
    while gearLoc != -1:
        gearsList.append(gearLoc + startSlice)
        startSlice += gearLoc + 1
        gearLoc = schemLine[startSlice:].find('*')

    return gearsList

def getGearRatio(gear, line):
    aroundList = []
    print(line, gear)
    for i in around:
        # print(i)
        # print(line[i[0]])
        if line[i[0]][gear+i[1]].isdigit():
            aroundList.append(i)
            for j in line:
                print(j)

            print(i)

    return 0

def processLineGears(schemList, i):
    ratioSum = 0
    gearIndexes = findGears(schemList, i)
    currentLine = [
        schemList[i-1],
        schemList[i],
        schemList[i+1]
    ]
    for gear in gearIndexes:
        ratioSum += getGearRatio(gear, currentLine)
    
    print(schemList[i], end='')
    print(gearIndexes)

    return ratioSum

    
def main():
    schematicList = prepareSchematic(schematic)
    processLineGears(schematicList, 2)
    sum = 0
    # for i in range(1,len(schematicList)-1):
    #     # sum += findNumber(schematicList, i)
    #     sum += processLineGears(schematicList, i)
    #     # print(schematicList[i])
    return sum

print(main())
# print([0,1] + [2,3])
test = ".........*.602.........571-.......................*...*.............199.....$.........181.......*......980....292............................."

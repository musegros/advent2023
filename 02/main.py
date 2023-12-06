import sys

bag = {
    "blue": 14,
    "red": 12,
    "green": 13
}

def getGameNumber(input):
    spaceInd = input.find(' ')
    return int(input[spaceInd:colonInd])

def parseGameItem(item, leastSet):
    colorList = item.strip().split(',')
    for color in colorList:
        colorList = color.strip().split(' ')
        amount = int(colorList[0])
        color = colorList[1]
        if color not in leastSet:
            leastSet[color] = amount
        elif leastSet[color] < amount:
            leastSet[color] = amount

    return leastSet

def getPower(inputSet):
    product = 1
    for key in inputSet.keys():
        product = product * inputSet[key]
    return product

def processLine(inputLine):
    inputLine = inputLine.replace('\n', '')
    colonInd = inputLine.find(':')
    gameList = inputLine[colonInd+1:].split(';')
    leastSet = {}
    for i in gameList:
        leastSet = parseGameItem(i, leastSet)
    print(gameList, leastSet)
    power = getPower(leastSet)
    return power

def main():
    f = open('input.txt','r')
    sum = 0
    for line in f.readlines():
        sum += processLine(line)
        print(sum)

# main()
test = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

# processLine(test)
main()
# print(getPower({'green': 2, 'blue': 4, 'red': 1}))
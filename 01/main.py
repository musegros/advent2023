import sys

words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def main():
    file = open('input.txt', 'r')
    # file = open('test.txt', 'r')
    sum = 0
    pause = True

    for i in file.readlines():
        oldI = i
        i = parse(i)
        first = ""
        second = "" 
        for char in i:
            if char.isdigit():
                if first == "":
                    first = char
                    second = char
                else:
                    second = char
        sum += int(first + second)
        print(first, second, end=' - ')
        print(oldI.replace('\n', ''))
        print("      " + i.replace('\n',''))
              
        # print(sum)
    print(sum)


def parse(inputLine):
    justifyLen = len('startIndex=0 - ')
    replaceList = []
    for key in words.keys():
        tempInput = inputLine
        startIndex = 0
        while tempInput.find(key) != -1:
            localWordStart = tempInput.find(key)
            globalWordStart = startIndex + localWordStart
            replaceList.append([globalWordStart,globalWordStart+len(key), words[key]])
            startIndex = globalWordStart + len(key)
            tempInput = inputLine[startIndex:]

    replaceList.sort()
    # print(replaceList)
    if not len(replaceList):
        return inputLine

    for i in range(1,len(replaceList)):
        if replaceList[i][0] < replaceList[i-1][1]:
            replaceList[i-1][1] = replaceList[i][0]
    
    start = 0
    newString = ""
    for item in replaceList:
        newString += inputLine[start:item[0]] + str(item[2])
        start = item[1]
    
    newString += inputLine[replaceList[-1][1]:]

    return newString
    
    inputLine = inputLine[:earliest] + str(words[replaceWord]) + inputLine[earliest+len(replaceWord):]
            
a = 'tm18zstdjqjncnkpkknz1one357'
b = 'tmoneightzstdjqjncnkpkknzoneonethreefive7'
c = b
# print(c)
print(parse(c))
main()
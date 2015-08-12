from collections import defaultdict
# @param {string} s
# @param {string} t
# @return {string}

def minWindow(letters, t):
    if len(t) > len(letters):
        return ""
    needToFind = {}
    numNeedToFind = len(t)
    for i in t:
        if i in needToFind:
            needToFind[i] += 1
        else:
            needToFind[i] = 1

    hasFound = defaultdict(int)
    minRange = len(letters) + 1
    numFounded = 0
    minCord = (0,0)
    start = 0

    for i in range(len(letters)):
        letter = letters[i]
        if letter in needToFind:
            hasFound[letter] += 1
            if hasFound[letter] <= needToFind[letter]:
                numFounded += 1

        if numFounded == numNeedToFind:
            startLetter = letters[start]
            while (startLetter not in hasFound) or (hasFound[startLetter] > needToFind[startLetter]):
                if startLetter in hasFound and hasFound[startLetter] > needToFind[startLetter]:
                    hasFound[startLetter] -= 1
                start += 1
                startLetter = letters[start]

            if i-start < minRange:
                minRange = i-start
                minCord = (start,i)

    if minRange == len(letters) + 1 :
        return ""
    else:
        return letters[minCord[0]:minCord[1]+1]

S = "ab"
T = "A"
print minWindow(S,T)
__author__ = 'cenk'

from collections import defaultdict
import copy

def findSubstring(s, words):
    if len(s) == 0 or len(words) == 0:
        return []

    wordDict = defaultdict(int)

    length = 0
    wordSize = len(words[0])

    for i in words:
        length += len(i)
        wordDict[i] += 1

    tmpDict = defaultdict(int)
    result = []
    i = 0
    while i < len(s):
        j = i
        tmpDict.clear()
        while s[j:j+wordSize] in wordDict:
            tmpDict[s[j:j+wordSize]] += 1
            if tmpDict[s[j:j+wordSize]] > wordDict[s[j:j+wordSize]]:
                break
            elif tmpDict == wordDict:
                result.append(i)
                tmpDict.clear()
                break
            j += wordSize
        if len(s) - i < length:
            break
        i += 1
    return result

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# s = "barfoothefoobarman"
# words =  ["foo", "bar"]
# s = "aaaa"
# words = ["a","a","a","a","a","a","a"]
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]

print findSubstring(s,words)
__author__ = 'cenk'


def groupAnagrams(strs):
    results = []
    dict = {}
    for i in range(len(strs)):
        sortedS = "".join(sorted(strs[i]))
        if str(sortedS) in dict.keys():
            dict[str(sortedS)].append(i +1)
        else:
            dict[str(sortedS)] = []
            dict[str(sortedS)].append(i + 1)

    for i in dict.keys():
        results.append(dict[i])

    return results


def isAnagram(s, t):
    s = s.strip(" ")
    t = t.strip(" ")

    if len(s) != len(t):
        return False

    dict = {}
    for i in s:
        if dict.has_key(i):
            dict[i] += 1
        else:
            dict[i] = 1

    for i in t:
        if not dict.has_key(i):
            return False
        elif dict.has_key(i) and dict[i] <= 0:
            return False
        else:
            dict[i] -= 1

    for i in dict.values():
        if i != 0:
            return False

    return True


a = ["cat","dog", "god", "tca"]
print groupAnagrams(a)
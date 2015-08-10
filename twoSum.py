__author__ = 'cenk'


# def twoSum2(nums, target):
#     s = set(nums)
#
#
#     firstVal = 0
#     firstKey = 0
#     isSelf = False
#
#     for key,val in enumerate(nums):
#         if (target - val) in s:
#             if target - val == val:
#                 if isSelf:
#                     firstVal = val
#                     firstKey = key
#                     break
#                 isSelf = True
#
#             else:
#                 firstVal = val
#                 firstKey = key
#                 break
#
#     for i in range(firstKey,len(nums)):
#         if nums[i] == target - firstVal:
#             return firstKey, i

def twoSum(nums, target):
    dict = {}

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = [i]
        else:
            dict[nums[i]].append(i)
    result = []
    for index,i in enumerate(nums):
        if dict.has_key(target - i):
            for k in dict[target - i]:
                if index != k and index + 1 < k + 1:
                    result.append((index + 1,k+ 1 ))

    if len(result) == 0:
        return []
    else:
        result = sorted(result,key=lambda a: a[1])
        return result[0]

numbers= [ 1,1,1 ]
target= 2
print twoSum(numbers,target)
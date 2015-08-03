__author__ = 'cenk'

def quickSelect(arr,k):
    less =[]
    more = []
    pivot = arr[0]

    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)

    if k <= len(less):
        return quickSelect(less,k)
    elif k > len(arr) - len(more):
        return quickSelect(more,k - (len(arr) - len(more)))
    else:
        return pivot

a = [120,100,22,43,11,5,76,89]
print quickSelect(a,3)

def quickSort(arr):
    quickSortHelper(arr,0,len(arr) -1)

def quickSortHelper(arr,lo,hi):
    if lo < hi:
        pIndex = partition(arr,lo,hi)
        quickSortHelper(arr,lo,pIndex - 1)
        quickSortHelper(arr,pIndex + 1,hi)

def QuickSelect(arr,k):
    return QuickSelectHelper(arr,k - 1,0,len(arr) - 1)

def QuickSelectHelper(arr,k,lo,hi):
    index = partition(arr,lo,hi)

    if index < k:
        return QuickSelectHelper(arr,k,lo,index - 1)
    elif index > k:
        return QuickSelectHelper(arr,k - (index),index + 1,hi)
    else:
        return arr[index]

def partition(arr,lo,hi):

    pivotValue = arr[lo]
    pivotIndex = lo

    left = lo + 1
    right = hi
    done = False

    while not done:
        while left <= right and arr[left] <= pivotValue:
            left += 1
        while left <= right and pivotValue <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
    tmp = arr[right]
    arr[right] = arr[pivotIndex]
    arr[pivotIndex] = tmp
    return right


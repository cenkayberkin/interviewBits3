from collections import deque

def maxSlidingWindow1(nums, k):
    q = deque()
    max_numbers = []

    for i in xrange(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)

    for i in xrange(k, len(nums)):
        max_numbers.append(nums[q[0]])

        while q and nums[i] >= nums[q[-1]]:
            q.pop()

        while q and q[0] <= i - k:
            q.popleft()

        q.append(i)

    if q:
        max_numbers.append(nums[q[0]])

    return max_numbers

def maxSlidingWindow2(nums,k):
    dq = deque()
    ans = []
    for i in range(len(nums)):
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans

a = [1,3,-1,-3,5,3,6,7]
print maxSlidingWindow1(a,3)
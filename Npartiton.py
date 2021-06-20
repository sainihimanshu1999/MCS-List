import heapq
from heapq import *


def subset(nums, n):
    heap = [(0, i) for i in range(n)]
    res = [[] for _ in range(n)]

    for num in sorted(nums, reverse=True):
        val, idx = heappop(heap)
        total = val + num
        res[idx].append(num)

        heappush(heap, (total, idx))

    return res



arr = [1,2,3,4,5]
n = 3
print(subset(arr,n))
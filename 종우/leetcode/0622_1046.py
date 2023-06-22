# https://leetcode.com/problems/last-stone-weight/description/

# my solution using heapq

from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        print(stones)
        pq = []
        for stone in stones:
            heappush(pq, -stone)
        
        while len(pq) > 1:
            r1 = heappop(pq)
            r2 = heappop(pq)
            if r1 < r2:
                heappush(pq, r1-r2)
                
            
        if len(pq) == 0:
            return 0
        return -heappop(pq)
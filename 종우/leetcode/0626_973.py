# https://leetcode.com/problems/k-closest-points-to-origin/
# heap, pq

from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        answer = []
        for p in points:
            d = (p[0]**2 + p[1]**2)**(1/2)
            heappush(pq, (d, p))
        
        for i in range(k):
            answer.append(heappop(pq)[1])
        return answer        
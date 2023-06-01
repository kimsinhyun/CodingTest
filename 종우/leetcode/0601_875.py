# https://leetcode.com/problems/koko-eating-bananas/

# my attempt at solution
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # 1. eating bananas from each pile
        # 2. searching for the minimum integer(binary search)
        l = 1
        r = max(piles)
        answer = r

        while l <= r:
            k = (l + r) // 2
            if eatable(k, h, piles):
                r = k - 1
                answer = min(answer, k)
            else:
                l = k + 1

        return answer

def eatable(k, h, piles):
    tmp = 0
    for pile in piles:
        tmp += math.ceil( pile / k)
    if tmp <= h:
        return True
    return False

s = Solution()
print(s.minEatingSpeed([30,11,23,4,20], 6))
print(s.minEatingSpeed([3,6,7,11], 8))
print(s.minEatingSpeed([30,11,23,4,20], 5))
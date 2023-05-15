# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        left = [0]*n
        right = [0]*n
        left[0] = 1
        right[-1] = 1
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right[-i-1] = right[-i] * nums[-i]
        for i in range(n):
            answer[i] = right[i]*left[i]


        return answer
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int: # type: ignore comment;
        left, right = 0, len(height)-1
        water = 0
        while left < right:
            contains = min(height[left], height[right]) * (right-left)
            if contains > water:
                water = contains
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return water
    
# optimized
class Solution:
    def maxArea(self, height: List[int]) -> int: # type: ignore comment;
        left, right = 0, len(height)-1
        tallest = max(height)
        water = 0
        
        while left < right:
            water = max(water, min(height[left], height[right]) * (right-left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

            if (right-left)*tallest < water:
                break

        return water
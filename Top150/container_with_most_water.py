# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        max_vol = 0
        
        p1, p2 = 0, n-1
        while p1<p2:
            max_vol = max(max_vol, (p2-p1)*min(height[p1],height[p2]))
            if height[p1] < height[p2]:
                p1 += 1
            else: 
                p2 -= 1
        
        return max_vol
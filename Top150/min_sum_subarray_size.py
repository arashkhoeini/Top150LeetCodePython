# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        size = float('inf')
        current = 0
        for right in range(0, n):
            current += nums[right]
            while current >= target:
                size = min(size, right-left +1)
                current -= nums[left]
                left += 1

        if size == float('inf'): return 0
        return size        
# https://leetcode.com/problems/contains-duplicate-ii/submissions/1451784282/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = dict()
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = i
            else:
                if (i - nums_dict[num]) <= k:
                    return True
                else:
                    nums_dict[num] = i
        return False
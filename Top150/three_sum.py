# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        tuples = set()
        for p3 in range(n):
            p1 = p3+1
            p2 = n-1
            while p1 < p2:
                if sorted_nums[p1] + sorted_nums[p2] == -sorted_nums[p3]:
                    tuples.add((sorted_nums[p3], sorted_nums[p1], sorted_nums[p2]))
                    p1 += 1
                elif sorted_nums[p1] + sorted_nums[p2] < -sorted_nums[p3]:
                    p1 += 1
                else:
                    p2 -= 1
        return list(tuples)
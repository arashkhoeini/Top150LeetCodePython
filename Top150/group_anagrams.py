# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            groups[sorted_word].append(word)
        
        return list(groups.values())
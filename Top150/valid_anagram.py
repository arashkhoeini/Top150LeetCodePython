# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = dict()
        for l in s:
            s_dict[l] = s_dict.get(l, 0) + 1
        
        t_dict = dict()
        for l in t:
            t_dict[l] = t_dict.get(l, 0) + 1
        
        for l in s:
            if s_dict[l] != t_dict.get(l, 0):
                return False
        return True
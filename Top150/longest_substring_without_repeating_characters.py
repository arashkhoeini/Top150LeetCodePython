# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

# Given a string s, find the length of the longest 
# substring
# without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        size =  0
        chars = set()
        n = len(s)
        for right in range(0,n):
            if s[right] not in chars:
                chars.add(s[right])
                size = max(size, right-left+1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])
        return size
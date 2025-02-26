# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        result = True
        for c in s:
            
            while True:
                if i == len(t):
                    result = False
                    break
                if c == t[i]:
                    i += 1
                    break
                else:
                    i +=1    
            if not result:
                break
        return result
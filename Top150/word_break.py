# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150


# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def backtrack(s):
            if s in memo: return memo[s]
            if s in wordDict: return True
            
            for w in wordDict:
                if s.startswith(w) and backtrack(s[len(w):]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        memo = {}
        wordDict = set(wordDict)
        result = backtrack(s)
        return result

       
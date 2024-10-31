# https://leetcode.com/problems/ransom-note/submissions/1439178810/?envType=study-plan-v2&envId=top-interview-150

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = dict()
        for letter in magazine:
            magazine_dict[letter] = magazine_dict.get(letter, 0) + 1
        
        note_dict = dict()
        for letter in ransomNote:
            note_dict[letter] = note_dict.get(letter, 0) + 1

        for letter in ransomNote:
            if note_dict[letter] > magazine_dict.get(letter, 0):
                return False
        return True
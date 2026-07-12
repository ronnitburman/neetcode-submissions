class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of both the strings dont match - return false
        #sort both the strings
        #if both the strings match its an anagram

        if len(s)!=len(t):
            return False
        
        return sorted(s)==sorted(t)
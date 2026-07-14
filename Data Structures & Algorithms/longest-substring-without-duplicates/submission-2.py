class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=1
        longest=1
        if len(s)<1:
            return 0
        else:
            while j <= len(s):
                substring=s[i:j]
                if len(substring)!=len(set(substring)):
                    i+=1
                longest = max(longest, (j-i))             
                j+=1
        return longest

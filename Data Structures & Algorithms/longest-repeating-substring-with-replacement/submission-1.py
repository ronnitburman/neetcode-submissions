class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I will be using a sliding window technique where i use 2 pointers and keep a count of characters that are repeating
        # the window is valid if the len of the window is equal or less than the countof max recurring character + K

        l=0
        resp=1
        count={}

        for r in range(len(s)):
            length = r-l+1
            count[s[r]]=count.get(s[r],0)+1
            max_count = max(count.values())

            if length-max_count > k:
                # count[s[l]] = max(0, count[s[l]]-1)
                count[s[l]] -= 1
                l+=1 #think about edge case around here later
                
            resp = max(resp, (r-l+1))
        
        return resp

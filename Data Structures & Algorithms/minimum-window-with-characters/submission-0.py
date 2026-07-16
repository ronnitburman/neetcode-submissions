class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resp = ""
        i=0
        shortest = len(s)
        found_flag = False
        while i < len(s):
            if s[i] not in t:
                i+=1
                continue
            temp=t
            j=i
            while j<len(s) and temp:
                # print(f"j: {s[j]} temp: {temp}")
                if s[j] in temp:
                    # print("yes")
                    temp=temp.replace(s[j],"",1)
                j+=1
            if not temp:
                # print(f"shortest:{shortest} len: {j-i}")
                if shortest >= (j-i):
                    shortest = j-i
                    resp = s[i:j]
            i+=1
        return resp
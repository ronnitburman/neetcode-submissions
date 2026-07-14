class Solution:

    def encode(self, strs: List[str]) -> str:
        #if i use just a delimiter then there is a chance that the delimiter might be present in the code as well and might break the code
        #so i am going to have an int before the delimiter so that i know how many characters to parse
        resp_str=""
        for string in strs:
            resp_str += str(len(string)) + "#" + string
            #["ronnit","roy", "burman"]-> "6#ronnit3#roy6#burman"
        return resp_str
    def decode(self, s: str) -> List[str]:
        resp_list=[]
        i=0
        j=0
        while j < len(s):
            if s[j]=="#":
                len_int=j+1+int(s[i:j])
                resp_list.append(s[(j+1):len_int])
                i=j=len_int
            else:
                j+=1
        return resp_list

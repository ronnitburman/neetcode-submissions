class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #idea is that if the string is sorted, they should match if they are anagram
        #create a dict with the sorted anagram as the key and values being a list where i keep adding the anagrams
        #finally return the doct.values()
        resp_dict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in resp_dict:
                resp_dict[sorted_string].append(string) 
            else:
                resp_dict[sorted_string]=[string]
        
        return list(resp_dict.values())
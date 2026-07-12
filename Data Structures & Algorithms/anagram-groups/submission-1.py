class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so in order for them to be anagram, they have to be same in length and should match after being sorted
        #in a loop sort all words
        #go at each word and check for all the matches in the list and add it to response list
        response_dict={}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in response_dict.keys():
                response_dict[sorted_string].append(string)
            else:
                response_dict[sorted_string]=[string]
        return list(response_dict.values())        
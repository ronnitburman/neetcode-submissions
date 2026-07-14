class Solution:
    def isPalindrome(self, s: str) -> bool:
        #process the string to remove any non alphanumeric character
        #match the first half to second for palindrome
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s+=char.lower()        
        return new_s==new_s[::-1]
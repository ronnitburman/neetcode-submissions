class Solution:
    def isPalindrome(self, s: str) -> bool:
        #process the string to remove any non alphanumeric character
        #match the first half to second for palindrome
        new_s = s.lower()
        new_s = "".join(char for char in new_s if char.isalnum())        
        return new_s==new_s[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        #create a stack (LIFO) to add given characters
        #if the corresponding closing character is not present or the stack is not empty by the end of the loop, it is not valid
        stack=[]
        char_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in char_map.values():
                stack.append(char)
            elif char in char_map:
                if not stack:
                    return False
                temp = stack.pop()
                if temp!=char_map.get(char, ""):
                    return False
            
        return not stack


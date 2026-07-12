class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set should have unique elements
        #so if the length of the set of nums dont match len of list nums then it has dublicate
        return len(set(nums))!=len(nums)
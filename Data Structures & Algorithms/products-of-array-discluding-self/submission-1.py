class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #initially i was thinking about the division operator but then i saw that the division operator is not permitted
        #so basically i have to find a way to multiply the product to the left of the item and to the right of the item. maybe store it in a list and then do a final pass to send the products
        #intial method passed but it wasnt the most efficient. so thought of doing everything in 1 pass manipulating the values in place
        left_mult=[]
        right_mult=[]
        res=[1]*len(nums)
        left_multiplier=1
        right_multiplier=1
        for i,num in enumerate(nums):
            res[i]*=left_multiplier
            # left_mult.append(left_multiplier)
            left_multiplier*=nums[i]

            res[-(i+1)]*=right_multiplier
            right_multiplier*=nums[-(i+1)]

        return res


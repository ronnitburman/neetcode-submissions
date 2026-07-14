class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #initially i was thinking about the division operator but then i saw that the division operator is not permitted
        #so basically i have to find a way to multiply the product to the left of the item and to the right of the item. maybe store it in a list and then do a final pass to send the products

        left_mult=[]
        right_mult=[]
        res=[]
        left_multiplier=1
        right_multiplier=1
        for num in nums:
            
            left_mult.append(left_multiplier)
            left_multiplier*=num
            
        for num in nums[::-1]:
            right_mult.append(right_multiplier)
            right_multiplier*=num
        right_mult = right_mult[::-1]

        for i in range(len(nums)):
            res.append(left_mult[i]*right_mult[i])
        return res


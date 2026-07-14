class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #need to use a hashmap to check if there is member to the left of the number present in the set to mark the start of a sequence
        #then we just need to keep iterating for the loop to see how long the sequence continues if the element is the start of the sequence
        #the first solution passed, now lets try to optimize for space
        hash_set = set(nums)
        max_len = 0
        def is_seq_starter(num):
            return not((num-1) in hash_set)
        def len_of_seq(num):
            count=0
            j=num
            while j in hash_set:
                count+=1
                j+=1
            return count


        for num in nums:
            if is_seq_starter(num):
                max_len=max(max_len, len_of_seq(num))
        return max_len

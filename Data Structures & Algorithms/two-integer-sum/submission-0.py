class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i will use a dict so that i can look up the idx there
        #I go through the list and subtract it from the target and check if it is in the dict
        #if the the target differense is in the the dict then i will return the idx for both
        seen_map={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in seen_map:
                return [seen_map.get(diff),i]
            seen_map[num]=i
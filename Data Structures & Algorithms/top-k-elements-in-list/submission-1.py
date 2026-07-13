class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first i have to create a map of all ints and their freq
        #transform that into a reverse map of frequencies to ints
        #because it is sorted, return the first K asked
        sol_dict={}
        transformed_sol_list=[[] for _ in range(len(nums)+1)]
        # print(f"transformed_sol_list: {transformed_sol_list}")
        for num in nums:
            sol_dict[num]=sol_dict.get(num,0) + 1
        for num, freq in sol_dict.items():
            # print(f"freq: {freq}")
            transformed_sol_list[freq].append(num)

        # we have to return top K non empty idxs
        # or am i missing something here usually something feels a bit complex there is usually a simple approach to that
        
        #actually for the freq list - it will only have max idx as the length of the nums array because that can be the max freq if all the elements were the same number:
        #for top k i will start from the back of the list and return elements until i reach k
        resp_list=[]
        # print(f"transformed_sol_list_filled: {transformed_sol_list}")
        for i in range(len(nums), 0, -1):
            # print(f"index: {i}")
            # print(f"resp_list: {resp_list}")
            for n in transformed_sol_list[i]:
                resp_list.append(n)
                
                if len(resp_list)==k:
                    return resp_list





        # transformed_dict = []
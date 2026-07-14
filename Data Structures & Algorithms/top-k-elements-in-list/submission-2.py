class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num] = count.get(num,0)+1
        resp_list = [[] for _ in range(len(nums)+1)]
        for key, val in count.items():
            resp_list[val].append(key)
        resp =[]
        for bucket in resp_list[::-1]:
            for n in bucket:
                resp.append(n)
                if len(resp)==k:
                    return resp

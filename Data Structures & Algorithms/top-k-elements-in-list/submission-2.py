class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        for num in nums:
            values[num] = 1 + values.get(num, 0) 
        
        results = []
        for key, value in values.items():
            results.append([value, key])
        results.sort()
                
        res = []
        while len(res) < k:
            res.append(results.pop()[1])
        
        return res
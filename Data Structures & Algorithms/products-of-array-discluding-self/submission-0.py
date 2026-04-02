import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        index = 0
        while len(result) < len(nums):
            current_list = nums.copy()
            current_list.pop(index)

            prod = math.prod(current_list)
            result.append(prod)  
            index = index + 1  

        return result        
            
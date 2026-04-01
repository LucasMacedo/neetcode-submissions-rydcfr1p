class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, (len(sorted_nums) - 1)

        while left < right:
            soma = sorted_nums[left][1] + sorted_nums[right][1]

            if soma == target:
                return sorted([sorted_nums[left][0], sorted_nums[right][0]])
            if soma > target:
                right = (right - 1)
            else:
                left = (left + 1)

        return[]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = list(sorted(set(nums)))
        counter = {}
        index = 0

        if len(nums_set) == 0:
            return 0

        current_counter = 0
        for i in range(len(nums_set)):
            if index not in counter:
                counter[index] = 1

            if nums_set[i - 1] == (nums_set[i] - 1):
                counter[index] = counter[index] + 1
            else:
                index += 1

        return max(counter.values())
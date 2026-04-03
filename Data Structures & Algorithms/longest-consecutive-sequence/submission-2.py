class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_point = []
        nums_set = sorted(set(nums))
        
        for i, value in enumerate(nums_set):
            prev = value - 1
            if prev not in nums_set:
                start_point.append({"index": i, "value": value})
    
        print(start_point)

        max_values = 0
        for index in range(len(start_point)):
            current = start_point[index]
            next_index = None
            if index + 1 < len(start_point):
                next_index = start_point[index + 1]
            
            count = 0
            if next_index:
                start = current['index']
                end = next_index['index'] 
                count = end - start
            else:
                start = current['index']
                count = len(nums_set) - start

            if count > max_values:
                max_values = count

        return max_values
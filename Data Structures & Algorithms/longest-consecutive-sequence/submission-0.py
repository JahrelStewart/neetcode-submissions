class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set(nums)          
        maxCount = 0
        for num in _set:
            if num - 1 not in _set:
                count = 1
                while num + count in _set:
                    count += 1
                maxCount = max(maxCount, count)

        return maxCount
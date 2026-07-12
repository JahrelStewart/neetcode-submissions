class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        _map = {}
        for i, num in enumerate(nums):
            if target - num in _map:
                return [_map[target - num], i] 
            _map[num] = i
        
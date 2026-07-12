class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for num in nums:
            myset.add(num)
        
        return len(myset) != len(nums)
         
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set = set()
        l,r,lgst = 0,0,0        
        while r < len(s):
            while s[r] in _set:
                lgst = max(lgst, r-l)
                _set.remove(s[l])
                l += 1   

            _set.add(s[r])            
            r += 1

        return max(lgst, r-l)

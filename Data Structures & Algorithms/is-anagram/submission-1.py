class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        _s, _t = {}, {}
        for i in range(0, len(s)):
            _s[s[i]] = 1 + _s.get(s[i], 0)
            _t[t[i]] = 1 + _t.get(t[i], 0)

        return _s == _t
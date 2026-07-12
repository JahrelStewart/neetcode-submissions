class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = [] # pair[i, tmp]

        for i, tmp in enumerate(temperatures):
            while stk and tmp > stk[-1][1]:
                si, stmp = stk.pop()
                res[si] = i - si
            stk.append([i, tmp])
        return res

            

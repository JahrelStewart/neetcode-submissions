class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i, tmp in enumerate(temperatures):
            ptr = i
            while temperatures[ptr] <= tmp:
                if ptr == len(temperatures)-1:
                    ptr = i
                    break
                ptr += 1  
            res[i] = ptr - i 
        
        return res

            

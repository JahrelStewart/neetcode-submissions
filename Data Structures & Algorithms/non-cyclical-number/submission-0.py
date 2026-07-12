class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            square = self.squareSum(n)
            if square in seen:
                return False
            else:
                seen.add(square)
            n = square

        return True
    
    def squareSum(self, n: int) -> int:
        out = 0

        while n:
            digit = n % 10
            out += digit ** 2
            n = n // 10

        return out
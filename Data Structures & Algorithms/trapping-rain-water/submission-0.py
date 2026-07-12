class Solution:
    def trap(self, height: List[int]) -> int:
        #rule of thumb: for each index, determine its max left and max right walls, then simply do min(max_left, max_right) - height[i]        
        
        l, maxL = 0, height[0]
        r, maxR = len(height) - 1, height[len(height) - 1]
        next = l
        out = 0

        while l < r:
            trap = min(maxL, maxR) - height[next]
            out += trap if trap >= 0 else 0

            if maxL < maxR:
                l += 1
                next = l
            else: 
                r -= 1
                next = r

            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])            

        return out
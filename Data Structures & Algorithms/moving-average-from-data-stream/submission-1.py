from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.sum = 0
        self.dq = deque()
        self.size = size
        
    def next(self, val: int) -> float:
        self.sum += val
        self.dq.append(val)
        if len(self.dq) > self.size:
            diff = self.dq.popleft()
            self.sum -= diff
        return self.sum/len(self.dq)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

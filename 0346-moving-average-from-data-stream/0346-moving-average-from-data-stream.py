class MovingAverage:

    def __init__(self, size: int):
        self.window = deque([])
        self.running = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.window) >= self.size:
            num = self.window.popleft()
            self.running -= num
        self.window.append(val)
        self.running += val
        return self.running / len(self.window)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
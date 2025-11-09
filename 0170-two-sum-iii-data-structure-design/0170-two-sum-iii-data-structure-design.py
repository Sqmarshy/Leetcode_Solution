class TwoSum:

    def __init__(self):
        self.data = set()
        self.repeat = set()

    def add(self, number: int) -> None:
        if number in self.data:
            self.repeat.add(number)
        self.data.add(number)

    def find(self, value: int) -> bool:
        for i in self.data:
            diff = value - i
            if diff == i:
                if i in self.repeat:
                    return True
            else:
                if diff in self.data:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
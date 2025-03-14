class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]
        return

    def get(self, key: str, timestamp: int) -> str:
        # No data
        if key not in self.data:
            return ""

        # Edge case, if minimum time of setting is later than timestamp
        value = self.data[key]
        if value[0][1] > timestamp:
            return ""

        # Binary Search dont work with below 3 elements
        if len(value) < 3:
            for val, time in value[::-1]:
                if time <= timestamp:
                    return val

        # Binary Search
        left, right = 0, len(value) - 1
        while left < right:
            mid = math.ceil((left + right) / 2)
            if value[mid][1] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return value[left][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
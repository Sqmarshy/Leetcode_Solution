class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.map = {}
        self.cmap = {}
        self.rmap = {}
        for i in range(len(foods)):
            curr = [-ratings[i], foods[i]]
            self.map[foods[i]] = cuisines[i]
            self.rmap[foods[i]] = ratings[i]
            if cuisines[i] in self.cmap:
                heapq.heappush(self.cmap[cuisines[i]], curr)
            else:
                self.cmap[cuisines[i]] = [curr]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.map[food]
        self.rmap[food] = newRating
        heapq.heappush(self.cmap[c], [-newRating, food])
        
    def highestRated(self, cuisine: str) -> str:
        while self.cmap[cuisine]:
            res = heapq.heappop(self.cmap[cuisine])
            if -res[0] == self.rmap[res[1]]:
                heapq.heappush(self.cmap[cuisine], res)
                return res[1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
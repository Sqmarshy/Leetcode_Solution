class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort(reverse = True)
        res = 0
        for i in players:
            done = False
            while trainers and not done:
                curr = trainers.pop()
                if i <= curr:
                    done = True
                    res += 1
        return res
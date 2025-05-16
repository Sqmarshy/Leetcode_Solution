class Solution:
    def hammer_dist(self, a, b): # Helper Function for hammering distance
        dist = 0
        for i in range(len(a)):
            dist += 1 if a[i] != b[i] else 0
        return dist

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        track = {words[i] : groups[i] for i in range(len(groups))}
        by_length = defaultdict(list)
        for word in words:
            by_length[len(word)].append(word)
    
        memo = {}
        def dp(start, idx, arr, prev):
            key = (idx, prev)
            if idx >= len(arr):
                return []
            
            if key in memo:
                return memo[key]
            
            take, no_take = [], []
            if not start:
                take = dp(True, idx + 1, arr, arr[idx]) + [arr[idx]]
            else:
                if self.hammer_dist(arr[idx], prev) == 1 and track[arr[idx]] != track[prev]:
                    take = dp(start, idx + 1, arr, arr[idx]) + [arr[idx]]
            
            no_take = dp(start, idx + 1, arr, prev)
            res = take if len(take) > len(no_take) else no_take
            memo[key] = res
            return res

        final = []
        for group in by_length.values():
            memo = {}
            curr = dp(False, 0, group, None)
            final = final if len(final) > len(curr) else curr
        
        return final[::-1]
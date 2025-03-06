class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        bfs = deque([beginWord])
        res = 0
        while bfs:
            res += 1
            n = len(bfs)
            for _ in range(n):
                word = bfs.popleft()
                if word == endWord:
                    return res

                for choice in wordList:
                    if choice in visited:
                        continue
                    visited.add(word)
                    to_add, diff = True, 0
                    for i in range(len(choice)):
                        if word[i] != choice[i]:
                            diff += 1
                        if diff > 1:
                            to_add = False
                            break
                    if to_add:
                        bfs.append(choice)
                        visited.add(choice)
        return 0
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        window = len(words[0])
        table = defaultdict(str)
        left = 0

        # Build a lookup table of all possible substrings of length 'window'
        for i in range(len(s)):
            if (i - left) + 1 < window:
                continue
            sample = s[left:i+1]
            table[left] = sample
            left += 1

        res = []
        cache = set()
        end = len(s) - (len(words) * window) + 1  # Last possible start index

        for i in range(end):
            sample = s[i:i + window * len(words) + 1]  # Extract possible concatenation
            if sample in cache:
                res.append(i)
                continue

            count = Counter(words)  # Track occurrences of each word
            total = len(words)  # Number of words left to match
            idx = i

            # Try matching words sequentially
            while idx < len(s) and count[table[idx]] > 0:
                total -= 1
                count[table[idx]] -= 1
                idx += window

            if total == 0:
                res.append(i)
                cache.add(sample)

        return res
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # create a sliding window that includes at least k element
        def at_least_k(word, k):
            substring_count = 0
            c_count = 0
            v_dict = Counter()
            lp = 0

            for i in range(len(word)):
                if word[i] in vowels:
                    v_dict[word[i]] += 1
                else:
                    c_count += 1

                while c_count >= k and len(v_dict) == 5:
                    substring_count += len(word) - i
                    # strink our window
                    if word[lp] in v_dict:
                        v_dict[word[lp]] -= 1
                        if v_dict[word[lp]] <= 0:
                            del v_dict[word[lp]]
                    else:
                        c_count -= 1

                    lp += 1
                
            return substring_count

        return at_least_k(word, k) - at_least_k(word, k+1)
from collections import Counter

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        indices_tokeep = [0]
        prev_counter = Counter(words[0])
        for i in range(1, len(words)):
            if Counter(words[i]) != prev_counter:
                prev_counter = Counter(words[i])
                indices_tokeep.append(i)
        return [words[i] for i in indices_tokeep]
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s1, s2 = "", ""
        for w in word1:
            s1 += w
        for w in word2:
            s2 += w
        return s1 == s2
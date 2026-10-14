class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0                      # position in s
        for c in t:
            if i < len(s) and c == s[i]:
                i += 1             # found the next letter we needed
        return i == len(s)         # did we find all of s, in order?
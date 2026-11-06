class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        longestcommonprefixlenght = 0
        for i in range(min(len(s1), len(s2), len(s3))):
            if s1[i] == s2[i] == s3[i]:
                longestcommonprefixlenght += 1
            else:
                break
        if longestcommonprefixlenght == 0:
            return -1
        return len(s1 + s2 + s3) - 3 * longestcommonprefixlenght
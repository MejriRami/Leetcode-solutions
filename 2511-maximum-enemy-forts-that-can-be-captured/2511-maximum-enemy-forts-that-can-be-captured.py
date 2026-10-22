class Solution:
    def captureForts(self, forts: list[int]) -> int:
        # find the longest run of zeros bounded by 1 on one side and -1 on the other
        ma = 0
        n = len(forts)
        for i in range(n):
            for j in range(i + 1, n):
                if forts[i] * forts[j] == -1:      # one is 1, the other is -1
                    for k in range(i + 1, j):
                        if forts[k] != 0:
                            break
                    else:                          # runs only if no break happened
                        ma = max(ma, j - i - 1)
        return ma
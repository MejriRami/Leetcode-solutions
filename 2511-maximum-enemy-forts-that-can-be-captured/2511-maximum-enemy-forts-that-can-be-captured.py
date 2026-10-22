class Solution:
    def captureForts(self, forts: list[int]) -> int:
        ma = 0
        last = -1  # index of the last non-zero fort
        for i, f in enumerate(forts):
            if f != 0:
                if last != -1 and forts[last] == -f:
                    ma = max(ma, i - last - 1)
                last = i
        return ma
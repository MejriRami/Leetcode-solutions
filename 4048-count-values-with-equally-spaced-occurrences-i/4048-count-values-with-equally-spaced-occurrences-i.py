from collections import defaultdict

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = defaultdict(list)
        for i, n in enumerate(nums):
            pos[n].append(i)
        total = 0
        for e in pos.keys():
            if len(pos[e]) == 3 and pos[e][0] < pos[e][1] < pos[e][2] and pos[e][2] - pos[e][1] == pos[e][1] - pos[e][0]:
                total += 1
        return total
from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        pw = []
        for e in nums:
            if e % k == 0:
                pw.append(e // k)
        pw = sorted(set(pw))
        i = 1
        while len(pw) > 0:
            if pw[0] == i:
                i += 1
                pw.pop(0)
            else:
                return k * i
        return k * i
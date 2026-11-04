from typing import List
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # ---------- 1. cost[i] = ops to make nums[i:i+x] all equal ----------
        lo, hi = SortedList(), SortedList()   # lo holds the smaller half (median = lo[-1])
        slo = shi = 0                          # running sums of lo and hi

        def balance():
            nonlocal slo, shi
            while len(lo) > len(hi) + 1:
                v = lo.pop(); slo -= v
                hi.add(v);    shi += v
            while len(lo) < len(hi):
                v = hi.pop(0); shi -= v
                lo.add(v);     slo += v

        def add(v):
            nonlocal slo, shi
            if not lo or v <= lo[-1]:
                lo.add(v); slo += v
            else:
                hi.add(v); shi += v
            balance()

        def remove(v):
            nonlocal slo, shi
            if v <= lo[-1]:
                lo.remove(v); slo -= v
            else:
                hi.remove(v); shi -= v
            balance()

        cost = [0] * (n - x + 1)
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                m = lo[-1]
                cost[i - x + 1] = (m * len(lo) - slo) + (shi - m * len(hi))

        # ---------- 2. DP: choose k non-overlapping windows ----------
        INF = float('inf')
        prev = [0] * (n + 1)              # j = 0 windows -> cost 0
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]                       # don't end a window here
                if i >= x and prev[i - x] != INF:
                    cur[i] = min(cur[i], prev[i - x] + cost[i - x])  # window nums[i-x:i]
            prev = cur

        return prev[n]
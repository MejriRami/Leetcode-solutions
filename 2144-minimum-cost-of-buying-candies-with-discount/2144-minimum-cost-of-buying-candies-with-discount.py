class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        free = 0
        for i in range(2, len(cost), 3):
            free += cost[i]
        return sum(cost) - free
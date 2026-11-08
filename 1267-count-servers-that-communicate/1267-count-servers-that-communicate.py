class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (grid[i].count(1) > 1 or [grid[k][j] for k in range(len(grid)) if k != i].count(1) > 0):
                    total += 1
                else:
                    continue
        return total
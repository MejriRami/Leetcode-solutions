class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i].count(1)==len(grid)-1:
                return i

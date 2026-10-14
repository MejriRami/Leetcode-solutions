class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total = 0
        adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h == 0:
                    continue          # empty cell: no faces at all
                total += 2            # top face + bottom face
                for di, dj in adjacents:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        neighbor = grid[ni][nj]
                    else:
                        neighbor = 0  # outside the grid counts as height 0
                    if h > neighbor:
                        total += h - neighbor
        return total
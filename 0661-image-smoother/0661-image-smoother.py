class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        n, m = len(img), len(img[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        result = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                total = img[i][j]
                count = 1  # include the cell itself

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        total += img[ni][nj]
                        count += 1

                result[i][j] = total // count

        return result
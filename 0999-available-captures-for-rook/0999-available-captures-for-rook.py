class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "R":
                    total = 0
                    # right, left, down, up
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        r, c = i + di, j + dj
                        while 0 <= r < rows and 0 <= c < cols:
                            if board[r][c] == "p":
                                total += 1
                                break
                            if board[r][c] == "B":
                                break
                            r += di
                            c += dj
                    return total
        return 0
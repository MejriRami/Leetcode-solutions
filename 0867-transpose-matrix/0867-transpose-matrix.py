class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(transpose)):
            for j in range(len(transpose[0])):
                transpose[i][j] = matrix[j][i]
        return transpose
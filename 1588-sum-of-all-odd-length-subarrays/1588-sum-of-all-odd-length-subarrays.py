class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)

        # prefix sums: prefix[i] = sum of arr[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total = 0
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                if length % 2 == 1:
                    total += prefix[j + 1] - prefix[i]

        return total
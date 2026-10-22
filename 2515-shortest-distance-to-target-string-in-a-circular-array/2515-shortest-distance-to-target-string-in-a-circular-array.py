class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        best = n  # larger than any possible distance

        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                best = min(best, d, n - d)

        return best if best < n else -1
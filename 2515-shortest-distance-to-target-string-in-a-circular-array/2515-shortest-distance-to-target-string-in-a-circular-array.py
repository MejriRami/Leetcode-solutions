class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        for step in range(n // 2 + 1):
            if words[(startIndex + step) % n] == target or words[(startIndex - step) % n] == target:
                return step
        return -1
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, total = 1, 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            if total + w > 100:   # letter doesn't fit
                lines += 1        # start a new line
                total = 0
            total += w
        return [lines, total]
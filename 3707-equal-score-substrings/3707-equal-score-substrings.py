class Solution:
    def charsum(self, s: str) -> int:
        ans = 0
        for ch in s:
            ans += ord(ch) - 96
        return ans

    def scoreBalance(self, s: str) -> bool:
        pointer = 0

        while pointer < len(s):
            leftsum = self.charsum(s[:pointer])
            rightsum = self.charsum(s[pointer:])

            if leftsum == rightsum:
                return True

            if leftsum < rightsum:
                pointer += 1
            else:
                return False

        return False
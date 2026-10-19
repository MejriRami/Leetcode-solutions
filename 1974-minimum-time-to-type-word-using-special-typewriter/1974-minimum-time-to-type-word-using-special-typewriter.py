class Solution:
    def minTimeToType(self, word: str) -> int:
        total = 0
        prev = 'a'                              # the pointer starts at 'a'
        for char in word:
            d = abs(ord(char) - ord(prev))      # distance going one way
            total += min(d, 26 - d) + 1         # shorter way around + 1 to type
            prev = char                         # pointer is now on this char
        return total
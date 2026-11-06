class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        newstring = ""
        for e in words:
            newstring += e[::-1]
            newstring += " "
        return newstring.strip()
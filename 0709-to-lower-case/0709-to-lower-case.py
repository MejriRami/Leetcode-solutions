"""class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower() 
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for e in s:
            result += e.lower()
        return result
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r"[a-z]+", paragraph.lower())
        counts = Counter(words)

        most_frequent = ""
        max_count = 0
        for word, count in counts.items():
            if count > max_count and word not in banned_set:
                max_count = count
                most_frequent = word
        return most_frequent
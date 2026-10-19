class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]           # key = height, value = name
        result = []
        for h in sorted(d, reverse=True):      # heights from tallest to shortest
            result.append(d[h])
        return result
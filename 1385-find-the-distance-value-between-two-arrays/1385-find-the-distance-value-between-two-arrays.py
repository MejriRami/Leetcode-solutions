class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance = 0
        for e in arr1:
            for j in arr2:
                if abs(e - j) <= d:
                    break
            else:
                distance += 1
        return distance
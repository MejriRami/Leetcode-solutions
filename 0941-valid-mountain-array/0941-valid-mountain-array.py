class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = arr.index(max(arr))      # index of the peak

        # Peak can't be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Strictly increasing up to the peak
        for j in range(0, i):
            if arr[j] >= arr[j + 1]:
                return False

        # Strictly decreasing after the peak
        for j in range(i, n - 1):
            if arr[j] <= arr[j + 1]:
                return False

        return True
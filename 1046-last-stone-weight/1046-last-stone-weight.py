class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            y = max(stones)        # heaviest stone
            stones.remove(y)
            x = max(stones)        # second heaviest stone
            stones.remove(x)
            if x != y:
                stones.append(y - x)
        return stones[0] if stones else 0
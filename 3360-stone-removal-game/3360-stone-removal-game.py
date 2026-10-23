class Solution:
    def canAliceWin(self, n: int) -> bool:
        sub = 10
        alice_turn = True
        while n >= sub:          # current player can make a move
            n -= sub
            sub -= 1
            alice_turn = not alice_turn
        # The player whose turn it is now can't move, so they lose
        return not alice_turn
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        count5 = 0
        count10 = 0
        count20 = 0
        for e in bills:
            if e == 5:
                count5 += 1
            if e == 10:
                if count5 == 0:
                    return False
                else:
                    count10 += 1
                    count5 -= 1
            if e == 20:
                if count10 > 0 and count5 > 0:
                    count20 += 1
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count20 += 1
                    count5 -= 3
                else:
                    return False
        return True
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def is_prime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        p = sum(is_prime(i) for i in range(1, n + 1))

        def fact(k):
            r = 1
            for i in range(2, k + 1):
                r = r * i % MOD
            return r

        return fact(p) * fact(n - p) % MOD
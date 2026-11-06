"""class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        arr = [0] * len(queries)
        serverlog = dict()
        for e in logs:
            if e[0] not in serverlog.keys():
                serverlog[e[0]] = [e[1]]
            else:
                serverlog[e[0]].append(e[1])
        intervales = []
        for e in queries:
            intervales.append([e - x, e])
        for k in range(len(intervales)):
            e = intervales[k]
            busy = 0
            for server in serverlog:
                for t in serverlog[server]:
                    if e[0] <= t <= e[1]:
                        busy += 1
                        break
            arr[k] = n - busy
        return arr
"""
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        arr = [0] * len(queries)
        logs.sort(key=lambda e: e[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        count = defaultdict(int)
        active = 0
        l = r = 0
        for i in order:
            q = queries[i]
            while r < len(logs) and logs[r][1] <= q:          # add logs entering window
                if count[logs[r][0]] == 0:
                    active += 1
                count[logs[r][0]] += 1
                r += 1
            while l < len(logs) and logs[l][1] < q - x:       # remove logs leaving window
                count[logs[l][0]] -= 1
                if count[logs[l][0]] == 0:
                    active -= 1
                l += 1
            arr[i] = n - active
        return arr
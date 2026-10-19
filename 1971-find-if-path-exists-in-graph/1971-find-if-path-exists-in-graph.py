"""class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        visited = []                      # moved OUTSIDE dfs so it's shared

        def dfs(edges: list[list[int]], source: int) -> bool:
            visited.append(source)
            if source == destination:     # check the current node
                return True
            for e in edges:
                if e[0] == source and e[1] not in visited:
                    if dfs(edges, e[1]):  # go deeper, pass the result up
                        return True
                elif e[1] == source and e[0] not in visited:
                    if dfs(edges, e[0]):  # edges go both ways
                        return True
            return False                  # no path from this node

        return dfs(edges, source)         # actually call dfs
    """
from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        stack = [source]                  # iterative DFS avoids recursion limits
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            stack.extend(graph[node])
        return False
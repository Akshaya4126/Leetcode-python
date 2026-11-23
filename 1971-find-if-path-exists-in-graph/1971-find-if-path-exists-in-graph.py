class Solution:
    def validPath(self, n, edges, source, destination):
        graph = [[] for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True

            return False

        return dfs(source)
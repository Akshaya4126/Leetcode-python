import heapq

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graph = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        pq = [(-1.0, start)]
        prob = [0.0] * n
        prob[start] = 1.0

        while pq:
            p, node = heapq.heappop(pq)
            p = -p

            if node == end:
                return p

            if p < prob[node]:
                continue

            for nei, w in graph[node]:
                new_prob = p * w

                if new_prob > prob[nei]:
                    prob[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))

        return 0.0
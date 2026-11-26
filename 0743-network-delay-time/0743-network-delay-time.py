import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}

        for u, v, w in times:
            graph.setdefault(u, []).append((v, w))

        pq = [(0, k)]
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)

            if node in dist:
                continue

            dist[node] = time

            for nei, wt in graph.get(node, []):
                if nei not in dist:
                    heapq.heappush(pq, (time + wt, nei))

        return max(dist.values()) if len(dist) == n else -1       
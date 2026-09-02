from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        # Create adjacency list
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        while queue:
            node = queue.popleft()

            # Destination reached
            if node == destination:
                return True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False
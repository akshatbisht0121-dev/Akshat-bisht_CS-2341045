class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n

        def dfs(node):
            # Already visiting -> cycle found
            if state[node] == 1:
                return False

            # Already determined to be safe
            if state[node] == 2:
                return True

            # Mark as currently visiting
            state[node] = 1

            # Check all neighbours
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            # No cycle found -> safe
            state[node] = 2
            return True

        answer = []

        for i in range(n):
            if dfs(i):
                answer.append(i)

        return answer
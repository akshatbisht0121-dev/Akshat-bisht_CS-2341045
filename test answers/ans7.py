def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    queue = [course for course in range(num_courses) if in_degree[course] == 0]
    order = []

    while queue:
        next_queue = []
        for course in queue:
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_queue.append(neighbor)
        queue = next_queue

    return order if len(order) == num_courses else []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result

# MAIN
n = int(input("Enter number of nodes: "))
graph = {}

print("Enter node connections (e.g., A B C for node A connected to B and C):")
for _ in range(n):
    parts = input().split()
    node = parts[0]
    edges = parts[1:]
    graph[node] = edges

start = input("Enter starting node for BFS: ").strip()

# Perform BFS
order = bfs(graph, start)
print("\nBFS Traversal Order:")
print(" -> ".join(order))

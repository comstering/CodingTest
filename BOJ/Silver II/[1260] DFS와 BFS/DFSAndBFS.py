from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])

    while queue:
        node = queue.popleft()
        visited[node] = True
        print(node, end=' ')

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, len(graph)):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

visited = [False] * (n + 1)
bfs(graph, v, visited)
print()


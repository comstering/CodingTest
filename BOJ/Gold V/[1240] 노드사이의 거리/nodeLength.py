def getLength(graph, visited, start, end):
    if start == end:
        return 0
    length = 0
    for i in graph[start]:
        if not visited[i[0]]:
            visited[i[0]] = True
            tmp = getLength(graph, visited, i[0], end)
            if tmp != -1:
                length += tmp + i[1]
            visited[i[0]] = False
    if length == 0:
        return -1
    return length


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n - 1):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

for _ in range(m):
    start, end = map(int, input().split())
    visited = [False] * (n+1)
    visited[start] = True
    print(getLength(graph, visited, start, end))

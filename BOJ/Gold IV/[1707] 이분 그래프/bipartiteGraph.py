import sys

sys.setrecursionlimit(10 ** 6)

def dfs(graph, node_v, node, check, color):
    node[node_v] = True

    check[node_v] = color % 2

    result = True
    for i in graph[node_v]:
        if not node[i]:
            result = result and dfs(graph, i, node, check, check[node_v] + 1)
        elif check[node_v] == check[i]:
            result = False
    return result


case = int(sys.stdin.readline())

for _ in range(case):
    v, e = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = True
    node = [False] * (v + 1)
    for i in range(v):
        if node[i + 1]:
            continue
        check = [2] * (v + 1)
        answer = answer and dfs(graph, i + 1, node, check, 0)

    if answer:
        print('YES')
    else:
        print('NO')
import sys
sys.setrecursionlimit(10 ** 6)

def lineLength(graph, node, visited):
    # 현재 노드 방문 처리
    visited[node[0]] = True
    length = 0
    lastNode = 0
    # 깊이 우선 탐색으로 가중치 길이 구하기
    for i in graph[node[0]]:
        if not visited[i[0]]:
            # 하나의 일직선 길이 구하기
            tmpLength, tmpNode = lineLength(graph, i, visited)
            tmpLength += i[1]
            # 현재 구해진 길이보다 길다면 tmp로 값 변경
            if tmpLength > length:
                length = tmpLength
                lastNode = tmpNode

    # 마지막 노드일 경우 자신의 노드 반환
    if length == 0:
        lastNode = node[0]
    return length, lastNode


n = int(input())
# n이 1이면 0 반환
if n == 1:
    print(0)
else:
    # graph 만들기
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n):
        pNode, cNode, weight = map(int, input().split())
        # 부모노드에 자식노드, 가중치 저장
        graph[pNode].append((cNode, weight))
        # 자식노드에 부모노드, 가중치 저장
        graph[cNode].append((pNode, weight))

    # leaf 노드 구하기
    leafNode = 0
    for i in range(n):
        if len(graph[i + 1]) == 1:
            leafNode = i + 1

    answer = 0

    # 첫 leaf 노드에서 가장 긴 경로의 leaf Node 구하기
    # 해당 leaf 노드에서 가장 긴 경로 구하기
    for _ in range(2):
        # 방문 처리 리스트
        visited = [False] * (n + 1)
        # 시작 노드 방문 처리
        visited[leafNode] = True

        # 시작 노드에 연결된 노드 방향으로 길이 구하기
        length = graph[leafNode][0][1]
        tmpLength, leafNode = lineLength(graph, graph[leafNode][0], visited)
        # 이전 길이보다 길 경우 answer 값 변경
        answer = length + tmpLength
    print(answer)

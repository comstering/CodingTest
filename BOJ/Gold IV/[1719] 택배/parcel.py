n, m = map(int, input().split())

# 거리 저장 그래프
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
# 거쳐가는 노드 저장 그래프
result = [[0] * (n + 1) for _ in range(n + 1)]

# 그래프 만들기
for _ in range(m):
    n1, n2, v = map(int, input().split())
    # 그래프 저장
    graph[n1][n2] = v
    graph[n2][n1] = v
    # 거쳐가는 노드 저장
    result[n1][n2] = n2
    result[n2][n1] = n1

# 플로이드 와샬 알고리즘
# 중간노드 반복
for middle in range(1, n + 1):
    # 시작노드 반복
    for start in range(1, n + 1):
        # 끝노드 반복
        for end in range(1, n + 1):
            # 시작노드와 끝노드가 같을 경우는 자기 자신이므로 0으로 표시
            if start == end:
                graph[start][end] = 0
                graph[end][start] = 0
            else:
                # 중간노드를 거쳐간 길이
                new_length = graph[start][middle] + graph[middle][end]
                # 중간노드를 거쳐간 길이가 현재 저장되어 있는 길이보다 짧을 경우
                if new_length < graph[start][end]:
                    # 길이 최신화
                    graph[start][end] = new_length
                    # 중간노드를 경유하는 경로의 첫 노드를 저장
                    result[start][end] = result[start][middle]

for i in result[1:]:
    print(' '.join(map(lambda x: str(x) if x != 0 else '-', i[1:])))

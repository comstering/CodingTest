import sys


class Tree:
    def __init__(self, n):
        self.graph = [[] for _ in range(n + 1)]
        self.visited = [False] * (n + 1)
        self.node = 1

    # 현재 노드에서 가장 먼 노드 구하기
    # 깊이우선탐색
    def lineLength(self, node):
        # 현재 노드 방문처리
        self.visited[node[0]] = True
        # 이전 노드에서 현재노드까지의 거리
        length = node[1]
        # 가장 먼 노드를 저장하기 위한 변수
        # 현재노드로 초기화
        v = node[0]

        # 현재 노드에 연결된 노드 탐색
        for n, e in self.graph[node[0]]:
            # 방문하지 않았던 노드만 탐색
            if not self.visited[n]:
                # 깊이우선탐색
                # 갈 수 있는 끝 노드번호와, 해당 노드까지의 거리
                tmp = self.lineLength((n, e))
                # 총 노드의 길이
                tmp_len = node[1] + tmp[1]
                # 이전의 탐색보다 현재 탐색의 길이가 길다면 결과 변경
                if length < tmp_len:
                    v = tmp[0]
                    length = tmp_len
        # 다음 탐색을 위해 현재 노드 방문처리 해제
        self.visited[node[0]] = False

        # 가장 먼 노드번호와 해당 노드까지의 거리 반환
        return v, length

    def getAnswer(self):
        answer = 0
        for _ in range(2):
            n = self.node
            # 현재 노드 방문처리
            self.visited[self.node] = True
            # 현재 노드와 연결된 노드 탐색
            for idx in self.graph[self.node]:
                # 가장 긴 거리의 노드 찾기
                tmp = self.lineLength(idx)
                # 현재의 답보다 길다면 결과 변경
                if tmp[1] > answer:
                    # 가장 먼 노드의 번호
                    n = tmp[0]
                    # 가장 먼 노드까지의 거리
                    answer = tmp[1]
            # 다음 탐색을 위해 현재 노드 방문처리 해제
            self.visited[self.node] = False
            # 새로운 시작노드를 가장 먼 노드로 변경
            self.node = n
        return answer


v = int(sys.stdin.readline())
tree = Tree(v)

# 트리 만들기
for _ in range(v):
    node_weight = list(map(int, sys.stdin.readline().split()))
    idx = 1
    while node_weight[idx] != -1:
        edge = (node_weight[idx], node_weight[idx + 1])
        tree.graph[node_weight[0]].append(edge)
        idx += 2

print(tree.getAnswer())

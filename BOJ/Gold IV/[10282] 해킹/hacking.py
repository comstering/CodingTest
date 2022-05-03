import sys, heapq


class Hack:
    def __init__(self, n):
        # 노드별 연결 그래프 리스트
        self.graph = [[] for _ in range(n + 1)]
        # 노드별 시간 리스트
        self.time_list = [float('inf')] * (n + 1)
        # 다익스트라 알고리즘 큐
        self.queue = []

    # 그래프에 연결 정보 추가하기
    def addEdge(self, a, b, s):
        self.graph[b].append((s, a))

    # 해킹 과정
    def hacking(self, computer):
        # 시작 노드의 시간 0
        self.time_list[computer] = 0
        # 시간을 우선순위로 두기 위해 (시간, 노드)
        heapq.heappush(self.queue, (0, computer))
        # 큐가 빌 때까지 반복
        while self.queue:
            # 시간, 노드
            current_time, current_node = heapq.heappop(self.queue)
            # 비용이 기록된 시간보다 길 경우 패스
            if self.time_list[current_node] < current_time:
                continue

            # 현재 노드에서 연결된 노드까지의 시간
            for t, node in self.graph[current_node]:
                # 다음 노드까지 걸리는 시간
                new_time = current_time + t
                # 구한 시간이 기존의 시간보다 짧을 경우 최단 시간 등록
                if new_time < self.time_list[node]:
                    self.time_list[node] = new_time
                    heapq.heappush(self.queue, (new_time, node))

    # 결과 출력
    def printAnswer(self, computer):
        # 해킹
        self.hacking(computer)
        answer = 0
        count = 0
        # 각 노드별 시간 탐색
        for i in self.time_list:
            # INF일 경우 감염 못한 노드
            if i == float('inf'):
                continue
            count += 1
            # 마지막에 감염되는 노드의 시간 저장
            answer = max(answer, i)
        # 최종 결과 출력
        print(count, answer)


for _ in range(int(sys.stdin.readline())):
    n, d, c = map(int, sys.stdin.readline().split())
    hack = Hack(n)
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        hack.addEdge(a, b, s)
    hack.printAnswer(c)
    del hack

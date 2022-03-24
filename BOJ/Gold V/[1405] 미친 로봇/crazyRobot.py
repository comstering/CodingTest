class CrazyRobot:
    def __init__(self, n, east, west, south, north):
        self.n = n
        self.east = east
        self.west = west
        self.south = south
        self.north = north

    def dfs(self, graph, nx, ny, now_per, next_per, n):
        if graph[ny][nx]:  # 이미 지나간 위치일 경우 단순 경로가 아니므로 0반환
            return 0
        elif next_per == 0:  # 다음 방향으로 갈 가능성이 없는 것이므로 0반환
            return 0
        elif n == 0:  # 단순경로의 마지막까지 도달했을 경우 해당 위치까지의 확률 반환
            return now_per * next_per
        else:
            graph[ny][nx] = True  # 현재 위치 도착 처리
            per = now_per * next_per  # 현재 위치까지 도달할 확률
            # 동서남북 모두 지나가기
            result = 0
            result += self.dfs(graph, nx + 1, ny, per, self.east, n - 1)  # 동쪽
            result += self.dfs(graph, nx - 1, ny, per, self.west, n - 1)  # 서쪽
            result += self.dfs(graph, nx, ny + 1, per, self.south, n - 1)  # 남쪽
            result += self.dfs(graph, nx, ny - 1, per, self.north, n - 1)  # 북쪽
            # 전부 탐색했을 경우 다음 탐색을 위해 다시 현재 위치 도착처리 취소
            graph[ny][nx] = False
            return result

    def returnAnswer(self):
        graph = [[False] * (2 * self.n + 1) for _ in range(2 * self.n + 1)]
        return self.dfs(graph, self.n, self.n, 1, 1, self.n)


n, east, west, south, north = map(int, input().split())

# 확률 소수점으로 변경
east, west, south, north = map(lambda x: x / 100, (east, west, south, north))

crazy_robot = CrazyRobot(n, east, west, south, north)

print(crazy_robot.returnAnswer())

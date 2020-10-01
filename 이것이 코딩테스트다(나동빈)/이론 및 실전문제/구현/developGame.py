n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 지나간 위치 표시를 위한 map
d = [[0] * m for _ in range(n)]
# 첫 위치는 지나간 위치로 인식
d[x][y] = 1

mapped = []
for i in range(n):
    mapped.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    # direction
    # 0: 북
    # 1: 동
    # 2: 남
    # 3: 서
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and mapped[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if mapped[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

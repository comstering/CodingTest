import sys
sys.setrecursionlimit(10 ** 6)

def find_end(adventure, visited, money, room, n):
    # 레프리콘일 경우
    if adventure[room][0] == 'L':
        if money < adventure[room][1]:
            money = adventure[room][1]
    # 트롤일 경우
    elif adventure[room][0] == 'T':
        money -= adventure[room][1]

    # 돈이 마이너스가 되면 실패
    if money < 0:
        return False

    # 최종 방에 도달했으면 성공
    if room == n:
        return True

    # DFS
    for i in adventure[room][2]:
        # 방문한 노드가 아닐 경우만 실행
        if not visited[i]:
            # 다음 노드 방문 처리
            visited[i] = True
            # 탐색
            if find_end(adventure, visited, money, i, n):
                return True
            # 탐색이 끝났으면 다른 탐색을 위해 다시 다음 노드 방문 처리 취소
            visited[i] = False

    return False


while True:
    n = int(input())
    if n == 0:
        break
    adventure = [[]]
    # 어드벤처 방 리스트 입력 받기
    for _ in range(n):
        tmp = list(input().split())
        alpha, cost = tmp[0], int(tmp[1])  # 방의 내용물(빈 방, 레프리콘, 트롤), cost
        adventure.append([alpha, cost, list(map(int, tmp[2:-1]))])  # [내용물, cost, [다음 방 list]]

    # 방문 기록
    visited = [False] * (n + 1)
    visited[1] = True

    if find_end(adventure, visited, 0, 1, n):
        print('Yes')
    else:
        print('No')

from collections import deque
import sys


t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline())
    num_list = list(sys.stdin.readline()[1:-2].split(','))
    # D의 개수가 입력된 수보다 많을 경우 error 출력
    if p.count('D') > n:
        print('error')
        continue
    # reverse시 앞에서 제거와 뒤에서 제거를 구분
    front_or_back = True
    # Deque 만들기
    q = deque(num_list)
    for command in p:
        # Reverse 명령일 경우 반대로 빼기
        if command == 'R':
            front_or_back = not front_or_back
        # Delete 명령일 경우 앞에서 뺄지 위에서 뺄지 구분
        if command == 'D':
            if front_or_back:
                q.popleft()
            else:
                q.pop()

    print(f'[{",".join(q if front_or_back else reversed(q))}]')

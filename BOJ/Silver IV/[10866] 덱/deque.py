import sys
from collections import deque

n = int(sys.stdin.readline())

d = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    try:
        if command[0] == 'push_front':
            d.appendleft(int(command[1]))
        elif command[0] == 'push_back':
            d.append(int(command[1]))
        elif command[0] == 'pop_front':
            print(d.popleft())
        elif command[0] == 'pop_back':
            print(d.pop())
        elif command[0] == 'size':
            print(len(d))
        elif command[0] == 'empty':
            print(int(len(d) == 0))
        elif command[0] == 'front':
            print(d[0])
        elif command[0] == 'back':
            print(d[-1])
    except IndexError:
        print(-1)
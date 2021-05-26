import sys
cmdCount = int(sys.stdin.readline())
stack = []
for i in range(cmdCount):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(int(not stack))
    elif cmd[0] == 'top':
        print(stack[-1] if stack else -1)

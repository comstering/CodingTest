
left = ['[', '(']
right = [']', ')']

while True:
    s = input()
    if s == '.':
        break
    stack = []
    result = True
    for i in s:
        if i in left:
            stack.append(i)
        elif i in right:
            if not stack:
                result = False
                break
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = False
                    break
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = False
                    break

    if stack:
        result = False

    print('yes' if result else 'no')

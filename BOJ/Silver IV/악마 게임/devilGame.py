m = input()
n = int(input())

result = 'No Jam'
result_g = 0

for i in range(n):
    w, g = input().split()
    g = int(g)
    if len(m) >= len(w):
        continue
    # 앞, 뒤에 추가되었을 경우
    if m in w:
        g /= (len(w) - len(m))
        if g > result_g:
            result = w
            result_g = g
    # 중간에 추가되었을 경우
    else:
        m_stack = list(reversed(m))
        w_stack = list(w)
        for i in w_stack:
            if m_stack[-1] == i:
                m_stack.pop()
            if len(m_stack) == 0:
                g /= (len(w) - len(m))
                if g > result_g:
                    result = w
                    result_g = g
                break
print(result)
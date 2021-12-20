m = input()
n = int(input())

result = 'No Jam'
result_g = 0

for i in range(n):
    w, g = input().split()
    g = int(g)
    if len(m) >= len(w):
        continue
    m_stack = list(reversed(m))
    w_stack = list(w)
    for j in w_stack:
        if m_stack[-1] == j:
            m_stack.pop()
        if len(m_stack) == 0:
            g /= (len(w) - len(m))
            if g > result_g:
                result = w
                result_g = g
            break
print(result)
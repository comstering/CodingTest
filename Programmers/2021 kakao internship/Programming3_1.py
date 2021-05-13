def solution(n, k, cmd):
    stack = []
    answer = 'O'*n
    for i in cmd:
        comm = i.split()
        if len(comm) > 1:
            term = int(comm[1])
            if comm[0] == 'D':
                k += (term + answer[k+1:k+term+1].count('X'))
            else:
                k -= (term + answer[k-term:k].count('X'))
            if k < 0:
                k = 0
            elif k >= n:
                k = n - 1
        else:
            if comm[0] == 'C':
                answer = answer[:k] + 'X' + answer[k+1:]
                stack.append(k)
                c = 1
                if k >= 7 or answer[k:].count('O') == 0:
                    while answer[k - c] == 'X':
                        c += 1
                    k -= c
                else:
                    while answer[k + 1] == 'X':
                        c += 1
                    k += c
            elif comm[0] == 'Z':
                idx = stack.pop()
                answer = answer[:idx] + 'O' + answer[idx+1:]
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))    # 'OOOOXOOO'
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))    # 'OOXOXOOO'
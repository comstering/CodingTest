def solution(n, k, cmd):
    stack = []
    table = [i for i in range(n)]
    for i in cmd:
        comm = i.split()
        if len(comm) > 1:
            if comm[0] == 'D':
                k += int(comm[1])
            else:
                k -= int(comm[1])
            if k < 0:
                k = 0
            elif k >= len(table):
                k = len(table) - 1
        else:
            if comm[0] == 'C':
                stack.append((k, table[k]))
                table.remove(table[k])
                if k >= len(table):
                    k = len(table) - 1
            elif comm[0] == 'Z':
                data = stack.pop()
                table.insert(data[0], data[1])
                if data[0] <= k:
                    k += 1
    answer = 'O' * n
    for i in stack:
        answer = answer[:i[1]] + 'X' + answer[i[1]+1:]
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))    # 'OOOOXOOO'
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))    # 'OOXOXOOO'
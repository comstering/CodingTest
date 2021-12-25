n = int(input())
result = int(input())

idx = [n // 2, n // 2]
snail_map = [[0] * n for i in range(n)]

ud_idx = (-1, 0, 1, 0)    # up, right, down, left
rl_idx = (0, 1, 0, -1)    # up, right, down, left

loce_idx = 0

check = 2
check_idx = 0
max_check = 1
max_check_idx = 0

result_idx = [0, 0]

for i in range(n * n):
    snail_map[idx[0]][idx[1]] = i + 1
    if i + 1 == result:
        result_idx[0], result_idx[1] = idx[0] + 1, idx[1] + 1
    idx[0] += ud_idx[loce_idx]
    idx[1] += rl_idx[loce_idx]
    max_check_idx += 1
    if max_check == max_check_idx:
        check_idx += 1
        max_check_idx = 0
        loce_idx += 1
        loce_idx = loce_idx if loce_idx < 4 else 0

    if check == check_idx:
        check_idx = 0
        max_check += 1

for i in snail_map:
    for j in i:
        print(j, end=' ')
    print()
print(result_idx[0], result_idx[1])
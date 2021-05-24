def solution(s):
    bracket = list(s)
    if len(bracket) % 2 != 0:
        return False
    if bracket[0] == ")":
        return False
    count = 0
    for i in bracket:
        if i == "(":
            count += 1
        if i == ")":
            count -= 1
        if count < 0:
            return False
    if count != 0:
        return False
    return True


num = int(input())
for i in range(num):
    print('YES' if solution(input()) else 'NO')
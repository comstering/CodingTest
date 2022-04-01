def passing(queen, idx, value):
    for i in range(idx):
        if queen[i] == value or abs(queen[i] - value) == (idx - i):
            return False
    return True

def nqueen(queen, idx, n):
    if idx == n:
        return 1

    result = 0
    for i in range(n):
        queen[idx] = i
        if passing(queen, idx, i):
            result += nqueen(queen, idx + 1, n)
    return result

def solution(n):
    queen = [0] * n
    return nqueen(queen, 0, n)
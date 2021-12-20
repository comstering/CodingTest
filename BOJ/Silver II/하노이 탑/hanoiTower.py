def solution(num):
    hanoi = [[i for i in range(num, 0, -1)], [], []]



num = int(input())
print(solution(num))
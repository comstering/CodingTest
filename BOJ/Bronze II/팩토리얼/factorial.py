def solution(num):
    result = 1
    for i in range(num):
        result *= (i + 1)
        while result % 10 == 0:
            result //= 10
    return result % 10


count = int(input())

for i in range(count):
    num = int(input())
    print(solution(num))
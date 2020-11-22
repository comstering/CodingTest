# 정수 배열과 정수 N이 주어지면, N번째로 큰 배열 원소를 찾으시오
def solution(arr, n):
    arr.sort()
    return arr[-n]


print(solution([-1, 3, -1, 5, 4], 2))    # 4
print(solution([2, 4, -2, -3, 8], 1))    # 8
print(solution([-5, -3, 1], 3))    # -5
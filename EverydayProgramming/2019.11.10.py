# 정수 배열과 타겟 숫자가 주어지면 합이 타겟값이 되는 두 원소의 인덱스를 찾기
def solution(arr, num):
    answer = []
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == num:
                return [i, j]


print(solution([2, 5, 6, 1, 10], 8))   # [0, 2]
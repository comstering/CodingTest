# 정수 배열이 주어지면 가장 큰 이어지는 원소들의 합을 구하시오.
def solution(arr):
    maxSum = arr[0]
    checkMax = 0
    for i in arr:
        checkMax += i
        checkMax = checkMax if checkMax > i else i
        maxSum = maxSum if checkMax < maxSum else checkMax
    return maxSum


print(solution([-1, 3, -1, 5]))    # 7: 3 + (-1) + 5
print(solution([-5, -3, -1]))    # -1: -1
print(solution([2, 4, -2, -3, 8]))    # 9: 2 + 4 + (-2) + (-3) + 8
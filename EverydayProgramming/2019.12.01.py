# 정수 배열이 주어지면 두번째로 큰 값을 프린트하시오
def solution(arr):
    arr.sort(reverse=True)
    setting = set(arr)
    if len(setting) < 2:
        return "Does not exit"
    else:
        return arr[1]


print(solution([10, 5, 4, 3, -1]))    # 5
print(solution([3, 3, 3]))    # Does not exist.
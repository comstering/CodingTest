def solution(arr):
    arr.remove(min(arr))
    answer = arr if len(arr) > 0 else [-1]
    return answer


print(solution([4, 3, 2, 1]))
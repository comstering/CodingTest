# 정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게 하라
# 단, 나누기 사용 금지
def solution(arr):
    answer = []
    for i in range(len(arr)):
        mul = 1
        for j in range(len(arr)):
            if i != j:
                mul *= arr[j]
        answer.append(mul)
    return answer


print(solution([1, 2, 3, 4, 5]))    # [120, 60, 40, 30, 24]
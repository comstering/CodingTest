# 정수 배열이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오
def solution(arr):
    answer = []
    zero = []
    for i in arr:
        if i == 0:
            zero.append(0)
        else:
            answer.append(i)
    return answer + zero


print(solution([0, 5, 0, 3, -1]))    # [5, 3, -1, 0, 0]
print(solution([3, 0, 3]))    # [3, 3, 0]
# 정수 N이 주어지면 N보다 작은 피보나치 수의 합을 구하여라
def solution(num):
    first = 0
    second = 1
    answer = 0
    while second < num:
        first, second = second, first + second
        if second % 2 == 0:
            answer += second
    return answer

print(solution(12))    # 10: 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10
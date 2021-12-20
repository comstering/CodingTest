def solution(N, m, M, T, R):
    """
    :param N: 하고자하는 운동 시간
    :param m: 현재 맥박, 최저 맥박
    :param M: 최고 맥박
    :param T: 운동 시 상승 맥박
    :param R: 휴식 시 하락 맥박
    :return: 총 운동시간(운동 시간 + 휴식 시간)
    """
    if m + T > M:
        return -1
    ti = 0
    now = m
    while N > 0:
        if now + T <= M:
            now += T
            N -= 1
        else:
            now -= R
        ti += 1
        now = now if now >= m else m
    return ti


N, m, M, T, R = map(int, input().split())
print(solution(N, m, M, T, R))

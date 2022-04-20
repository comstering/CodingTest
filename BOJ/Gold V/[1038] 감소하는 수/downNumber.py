def solution(num):
    # 각 자리 수 별 감소하는 수의 개수를 담은 리스트
    count_list = [[1] * 10 for _ in range(10)]

    # 감소하는 수의 총 개수
    max_count = 9

    # 감수하는 수의 개수 리스트에 개수 구해서 저장하기
    for i in range(1, 10):
        for j in reversed(range(10)):
            count_list[i][j] = sum(count_list[i - 1][:j])
            max_count += count_list[i][j]

    # 입력이 감소하는 수 범위 밖이면 -1 반환
    if num > max_count:
        return -1
    # 입력이 10보다 작거나 같으면 그대로 반환
    if num <= 10:
        return num
    last = True
    count = 9  # 감소하는 수 count
    length = 0  # 자리수 - 1
    idx = 0  # 시작하는 수
    while last:
        length += 1
        for i in range(10):
            # 현재의 count에 다음 count를 더한 것이 입력보다 큰지 확인
            last = (count + count_list[length][i]) < num
            if not last:
                # 시작하는 숫자 기록
                idx = i
                break
            count += count_list[length][i]

    # 최고 자리 수의 시작수 세팅
    answer = idx * (10 ** length)

    # 자리수를 역으로 내려오면서 감소하는 수 구하기
    for i in reversed(range(length)):
        for j in range(idx):
            # count가 입력보다 작으면 계속 다음 숫자 확인
            if count + count_list[i][j] < num:
                count += count_list[i][j]
            # count가 입력보다 넘으면 현재 숫자를 기록하고 다음 자리수로 넘어감
            else:
                idx = j
                answer += idx * (10 ** i)
                break
    return answer


n = int(input())
print(solution(n))

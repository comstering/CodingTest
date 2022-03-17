n = int(input())
p_list = list(map(int, input().split()))
m = int(input())

# n이 1일 경우에는 0만 가능
if n == 1:
    print(0)
else:
    min_p1 = min(p_list[1:])  # 0을 제외한 나머지 값을 중 최솟값
    min_p0 = min(p_list)  # 0~end까지 최솟값

    if m - min_p1 < 0:  # 0 이외의 가장 작은 수를 살 수 없으므로 무조건 정답은 0
        print(0)
    else:
        # 최솟값을 가지는 숫자 찾기
        idx = 0
        while p_list[idx + 1:].count(min_p1) != 0:
            idx += p_list[idx + 1:].index(min_p1) + 1

        num_list = [idx]

        # 0을 포함해서 최솟값을 가지는 숫자 찾기
        idx = -1
        while p_list[idx + 1:].count(min_p0) != 0:
            idx += p_list[idx + 1:].index(min_p0) + 1

        # 0을 포함한 최솟값을 가지는 숫자 개수 구하기
        num_count = (m - p_list[num_list[0]]) // p_list[idx]
        tmp_list = [idx] * num_count
        # 만들 수 있는 가장 긴 길이의 방 번호
        num_list.extend(tmp_list)

        idx = 0
        # 방 번호 길이 만큼 반복
        while idx < len(num_list):
            # 큰 수부터 확인
            for i in reversed(range(n)):
                if i <= num_list[idx]:  # 현재의 수보다 작아졌을 경우 break
                    break
                # 현재 인덱스의 수를 다른 수로 바꿨을 경우 m을 넘는 지 확인
                if p_list[i] + sum(map(lambda x: p_list[x], num_list[:idx] + num_list[idx + 1:])) <= m:
                    num_list[idx] = i
            idx += 1
        # 최종 결과 출력
        print(''.join(map(str, num_list)))

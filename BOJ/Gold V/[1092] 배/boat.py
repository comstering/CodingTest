n = int(input())
n_list = sorted(list(map(int, input().split())), reverse=True)  # 내림차순 정렬
m = int(input())
m_list = sorted(list(map(int, input().split())), reverse=True)  # 내림차순 정렬

if max(m_list) > max(n_list):  # 크레인으로 옮기지 못하는 상자가 있을 경우
    print(-1)
else:
    result = 0  # 최종 결과
    count = 0  # 옮긴 상자 수

    n_idx = [0] * n  # 크레인이 옮긴 상자 인덱스
    check = [False] * m  # 상자 옮겨진 유무
    while count < m:  # 상자가 전부 옮겨 질 때까지 반복
        for i in range(n):  # 크레인 개수만큼 반복
            while n_idx[i] < m:  # 박스 인덱스 확인
                # 아직 옮겨지지 않았고 크레인으로 옮길 수 있는 상자일 경우
                if not check[n_idx[i]] and n_list[i] >= m_list[n_idx[i]]:
                    check[n_idx[i]] = True  # 상자 옮겨짐 처리
                    count += 1  # 옮긴 상자 개수 +1
                    break  # 상자를 옮겼으니 while 반복문 탈출
                n_idx[i] += 1  # 옮길 수 있는 상자를 찾을 때 까지 인덱스 +1
        result += 1  # 시간 +1
    print(result)

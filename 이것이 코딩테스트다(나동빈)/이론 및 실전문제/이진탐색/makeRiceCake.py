# n: 떡 개수, m: 요청한 떡 길이
n, m = map(int, input().split())
# 각 떡의 개별 높이
h_list = list(map(int, input().split()))

# 이진탐색 시작점 끝점
start = 0
end = max(h_list)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in h_list:
        # 잘랐을 때의 떡의 양 계산
        total += x - mid if x > mid else 0
    # 떡의 양이 부족한 경우 더 많이 자르기(좌측 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(우측 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기서 result 기록
        start = mid + 1

# 정답 출력
print(result)
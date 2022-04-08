n, k = map(int, input().split())

# 물건 담는 리스트
things = []

for _ in range(n):
    # 물건 담기
    things.append(tuple(map(int, input().split())))

# DP를 위한 이차원 배열
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(k + 1):
        # 물건이 없을 때와 들 수 있는 무게가 0일 때는 0
        if i == 0 or j == 0:
            dp[i][j] = 0
        # 물건이 들 수 있는 무게일 때
        elif things[i - 1][0] <= j:
            # 현재의 보석의 가치와 현재 보석의 무게를 뺀 무게였을 때의 보석 가치를 더한 값과 이전 동일 무게였을 때의 보석 가치 비교
            # 더 큰 값을 남김
            dp[i][j] = max(things[i - 1][1] + dp[i - 1][j - things[i - 1][0]], dp[i - 1][j])
        # 현재 들 수 없는 무게일 때
        else:
            # 이전 동일 무게였을 때의 보석 가치와 동일
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])

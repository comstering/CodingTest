chess1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
chess2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

n, m = map(int, input().split())

chess = []
for i in range(n):
    chess.append(input())

min_count = 64
for i in range(n - 7):
    for j in range(m - 7):
        count = [0, 0]
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if chess[k][l] != chess1[k - i][l - j]:
                    count[0] += 1
                if chess[k][l] != chess2[k - i][l - j]:
                    count[1] += 1
        min_count = min(count) if min(count) < min_count else min_count

print(min_count)
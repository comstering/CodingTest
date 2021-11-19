white_piece = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]

for i, j in zip(piece, white_piece):
    print(i - j, end=' ')
def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(0, len(board)):
            if board[j][i - 1] != 0:
                if basket[-1:] == [board[j][i - 1]]:
                    answer += 2
                    basket = basket[:-1]
                else:
                    basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))    # 4
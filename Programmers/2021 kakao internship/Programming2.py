def check(table):
    for i in range(5):
        for j in range(5):
            if table[i][j] == 'P':
                if (j < 4 and table[i][j + 1] == 'P') or (i < 4 and table[i + 1][j] == 'P'):
                    return 0
                elif i < 4 and j < 4 and ((table[i][j + 1] == 'O' or table[i + 1][j] == 'O') and table[i + 1][j + 1] == 'P'):
                    return 0
                elif i > 0 and j < 4 and ((table[i][j + 1] == 'O' or table[i - 1][j] == 'O') and table[i - 1][j + 1] == 'P'):
                    return 0
                elif (j < 3 and table[i][j + 1] == 'O' and table[i][j + 2] == 'P') or (i < 3 and table[i + 1][j] == 'O' and table[i + 2][j] == 'P'):
                    return 0
    return 1


def solution(places):
    answer = []
    for i in places:
        answer.append(check(i))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))    # [1, 0, 1, 1, 1]
def solution(numbers, hand):
    answer = ''
    keyPad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left, right = '*', '#'
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            right = i
            answer += 'R'
        else:
            key = keyPad[i]
            nowL = keyPad[left]
            nowR = keyPad[right]
            temL = abs(key[0] - nowL[0]) + abs(key[1] - nowL[1])
            temR = abs(key[0] - nowR[0]) + abs(key[1] - nowR[1])
            if temL < temR:
                left = i
                answer += 'L'
            elif temR < temL:
                right = i
                answer += 'R'
            else:
                if hand == 'right':
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'
    return answer


print(solution([1, 3, 4, 5, 6, 2, 1, 4, 5, 9, 5], "right"))    # LRLLLRLLRRL
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))    # LRLLRRLLLRR
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))    # LLRLLRLLRL
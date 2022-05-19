n = int(input())
liquid_list = list(sorted(map(int, input().split())))

# 투포인터 탐색 인덱스
first, second = 0, n - 1
# 결과 담길 변수
answer = [0, 0]
# 두 용액의 특성값 저장 변수
result = float('inf')

while first < second:
    # 특성값
    tmp = liquid_list[first] + liquid_list[second]
    # 구해진 특성 값이 0에 더 가까울 경우
    if result > abs(tmp):
        answer = [liquid_list[first], liquid_list[second]]
        result = abs(tmp)

    # 특성값이 0보다 작을 경우
    if tmp < 0:
        first += 1
    # 특성값이 0보다 클 경우
    elif tmp > 0:
        second -= 1
    # 특성값이 0일 경우
    else:
        break

print(answer[0], answer[1])

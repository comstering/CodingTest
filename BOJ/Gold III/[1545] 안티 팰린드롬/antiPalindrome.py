word = sorted(input())
length = len(word)

# 짝수, 홀수에 따른 투포인트 시작 위치 지정
if length % 2 == 0:
    start, end = length // 2 - 1, length // 2
else:
    start, end = length // 2 - 1, length // 2 + 1

answer = True

# 투포인트 탐색
while start >= 0 and answer:
    # index 저장
    tmp = end
    # 팰린드롬일 경우 아닐때까지 반복
    while word[start] == word[tmp]:
        tmp += 1
        # 인덱스가 문자열 길이를 벗어났으면 안티 팰린드롬이 될 수 없음
        if tmp >= length:
            answer = False
            break
    if not answer:
        break
    # 팰린드롬 수 고치기
    word[end], word[tmp] = word[tmp], word[end]
    start -= 1
    end += 1

if answer:
    print(''.join(word))
else:
    print(-1)

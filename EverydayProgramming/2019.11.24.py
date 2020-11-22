# 주어진 string에 모든 단어를 거꾸로 하시오
def solution(st):
    arr = st.split()
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return " ".join(arr)


print(solution("abc 123 apple"))    # cba 321 elppa
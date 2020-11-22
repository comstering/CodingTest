# 길이가 같은 무자열 A와 B가 주어지면 A가 B로 1:1 암호화 가능한지 찾으시오
def solution(A, B):
    strA = list(A)
    strB = list(B)
    dic = {}
    for i in range(len(strA)):
        if dic.get(strA[i]) is not None:
            if dic[strA[i]] != strB[i]:
                return False
        else:
            dic[strA[i]] = strB[i]
    return True


print(solution("EGG", "FOO"))    # True: E->F, G->O
print(solution("ABBCD", "APPLE"))    # True: A->A, B->P, C->L, D->E
print(solution("AAB", "FOO"))
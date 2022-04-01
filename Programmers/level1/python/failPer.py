def solution(N, stages):
    answer = []
    per = []
    for i in range(1, N + 1):
        if len(stages) <= 0:
            per.append(0.0)
        else:
            fail = stages.count(i)
            per.append(fail / len(stages))
            stages = list(filter(lambda a: a != i, stages))
    st = per.copy()
    per.sort()
    per.reverse()
    for i in per:
        ind = st.index(i)
        answer.append(ind + 1)
        st[ind] = -1
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))    # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))    # [4, 1, 2, 3]
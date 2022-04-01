def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


part = ["leo", "kiki", "eden"]
comp = ["eden", "kiki"]
print(solution(part, comp))
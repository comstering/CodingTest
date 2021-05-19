N, M = map(int, input().split())
contact = [{i} for i in range(N + 1)]
for i in range(M):
    c1, c2 = map(int, input().split())
    contact[c1].update(contact[c2])
    contact[c2].update(contact[c1])
    for j in contact[c1]:
        contact[j].update(contact[c1])
    for j in contact[c2]:
        contact[j].update(contact[c2])
for i in contact[1:]:
    print(min(i), end=' ')
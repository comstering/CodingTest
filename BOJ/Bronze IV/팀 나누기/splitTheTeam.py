levels = sorted(list(map(int, input().split())))
team1, team2 = levels[0] + levels[-1], levels[1] + levels[2]
print(abs(team1 - team2))

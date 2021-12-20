card_color = []
card_value = []

for i in range(5):
    color, value = input().split()
    value = int(value)
    card_color.append(color)
    card_value.append(value)

score = 0
dum_score = 0
check_condition = False

dum_value = sorted(card_value)
max_value = max(card_value)
set_color = set(card_color)
set_value = set(card_value)

if len(set_color) == 1:
    # 1번 조건
    if dum_value[0] + 4 == dum_value[1] + 3 == dum_value[2] + 2 == dum_value[3] + 1 == dum_value[4]:
        dum_score = max_value + 900
        score = dum_score if score < dum_score else score

    # 4번 조건
    dum_score = max_value + 600
    score = dum_score if score < dum_score else score
    check_condition = True

# 5번 조건
if dum_value[0] + 4 == dum_value[1] + 3 == dum_value[2] + 2 == dum_value[3] + 1 == dum_value[4]:
    dum_score = max_value + 500
    score = dum_score if score < dum_score else score
    check_condition = True

if len(set_value) == 2:
    # 2번 조건
    for i in set_value:
        if card_value.count(i) == 4:
            dum_score = i + 800
    score = dum_score if score < dum_score else score

    # 3번 조건
    two_value = 0
    three_value = 0
    for i in set_value:
        if card_value.count(i) == 2:
            two_value = i
        if card_value.count(i) == 3:
            three_value = i
        dum_score = three_value * 10 + two_value + 700
    score = dum_score if score < dum_score else score
    check_condition = True

if len(set_value) == 3:
    two_value = []
    for i in set_value:
        # 6번 조건
        if card_value.count(i) == 3:
            dum_score = i + 400
        # 7번 조건 세팅
        if card_value.count(i) == 2:
            two_value.append(i)
    score = dum_score if score < dum_score else score

    # 7번 조건
    if len(two_value) > 0:
        dum_score = max(two_value) * 10 + min(two_value) + 300
    score = dum_score if score < dum_score else score
    check_condition = True

# 8번 조건
if len(set_value) == 4:
    for i in set_value:
        if card_value.count(i) == 2:
            dum_score = i + 200
            break
    score = dum_score if score < dum_score else score
    check_condition = True

# 9번 조건
if not check_condition:
    dum_score = max_value + 100
    score = dum_score if score < dum_score else score

print(score)

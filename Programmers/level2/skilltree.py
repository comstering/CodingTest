def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        answer += checkSkill(skill, i)

    return answer


def checkSkill(skill, skill_tree):
    check = [0] * len(skill)
    for i in skill_tree:
        cou = skill.find(i)
        if cou < 0:
            continue
        elif cou == 0:
            check[0] = 1
        else:
            if check[cou - 1] != 1:
                return 0
            check[cou] = 1
    return 1


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
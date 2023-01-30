# 0130_1
# https://school.programmers.co.kr/learn/courses/30/lessons/49993

# 내 풀이
def solution(skill, skill_trees):
    answer = 0
    for order in skill_trees:
        tskill = skill
        for s in order:
            if s in tskill:
                if s == tskill[0]:
                    tskill = tskill[1:]
                else:
                    answer -= 1
                    break
        answer+=1
    return answer


def solution(skill, skill_trees):
    """
    1. 가능한 스킬 트리
    """
    from collections import deque
    answer = 0
    for sk in skill_trees:
        q_skill = deque(skill)
        flag = True
        for s in sk:
            if s not in q_skill:
                continue
            else:
                if s == q_skill[0]:
                    q_skill.popleft()
                else:
                    flag=False
                    break
        if flag:
            answer+=1
            
                    
    return answer
# 0125_1
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

# 내 풀이

def solution(record):
    answer = []
    nicknames = {}
    actions = []
    # track actions with uid
    # track uid with nicknames
    for r in record:
        r2 = r.split(" ")
        if r2[0] == 'Enter':
            if r2[1] not in nicknames:
                nicknames[r2[1]] = r2[2]
            elif nicknames[r2[1]] != r2[2]:
                nicknames[r2[1]] = r2[2]
        elif r2[0] == 'Change':
            nicknames[r2[1]] = r2[2]
            continue
        actions.append((r2[0], r2[1]))
    for a in actions:
        if a[0] == 'Enter':
            answer.append(f"{nicknames[a[1]]}님이 들어왔습니다.")
        elif a[0] == 'Leave':
            answer.append(f"{nicknames[a[1]]}님이 나갔습니다.")
            
    return answer


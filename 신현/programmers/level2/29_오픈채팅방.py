def solution(record):
    user = dict()
    for r in record:
        if r[:5] != "Leave":
            state, uid, name = r.split()
            user[uid] = name
    answer = []
    for r in record:
        temp = r.split()
        if temp[0] == "Enter":
            answer.append(f"{user[temp[1]]}님이 들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(f"{user[temp[1]]}님이 나갔습니다.")
        
    
    return answer
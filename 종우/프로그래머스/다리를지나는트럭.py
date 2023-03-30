# 0219
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# nice
def solution(bridge_length, weight, truck_weights):
    answer = 1
    cw = 0
    on_bridge = [0]*bridge_length
    on_bridge[-1] = truck_weights.pop(0)
    cw += on_bridge[-1]
    tw = 0
    while(cw):
        sub = on_bridge.pop(0)
        cw -= sub
        if truck_weights:
            if cw + truck_weights[0] <= weight:
                tw = truck_weights.pop(0)
                on_bridge.append(tw)
                cw += tw
            else :
                on_bridge.append(0)
        answer += 1
    return answer
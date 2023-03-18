# 0318
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        diff = cut(i, wires.copy())
        if diff < answer:
            answer = diff            
    
    return answer

def cut(i, wires):
    l, r = wires.pop(i)
    net1 = [l]
    net2 = [r]
    while len(wires) != 0:
        for i, wire in enumerate(wires):
            if wire[0] in net1:
                net1.append(wire[1])
                wires.pop(i)
                break
            if wire[0] in net2:
                net2.append(wire[1])
                wires.pop(i)
                break
            if wire[1] in net1:
                net1.append(wire[0])
                wires.pop(i)
                break
            if wire[1] in net2:
                net2.append(wire[0])
                wires.pop(i)
                break
    return abs(len(net1)-len(net2))
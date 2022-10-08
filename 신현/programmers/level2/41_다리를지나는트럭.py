def func(passing):
    for i in range(len(passing)):
        passing[i]['left'] -= 1
    return passing
        
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    passed = deque([])
    passing = deque([])
    waiting = deque(truck_weights)
    time = 1
    #첫 차부터 우선 보내기
    w =  waiting.popleft()
    passing.append(dict(weight=w, left=bridge_length))
    
    while waiting or passing:
        if len(waiting) > 0:
            w = waiting[0]
            if sum([c['weight'] for c in passing]) + w <= weight and waiting:
                waiting.popleft()
                passing.append(dict(weight=w, left=bridge_length))
        passing = func(passing)
        if passing[0]['left'] <= 0:
            passed.append(passing[0])
            passing.popleft()
        time+=1
    return time
    # test = deque([])
    # test.append(dict(car=10, num=10))
    # test.append(dict(car=20, num=20))
    # test.append(dict(car=30, num=30))
    # temp = sum([d['car'] for d in test])
    # print(temp)
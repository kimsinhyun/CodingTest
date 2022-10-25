def t2m(time):
    H, M = map(int,time.split(":"))
    return H*60 + M
def fee(time, fees):
    import math
    dt, df, ut, uf = fees
    total_fee = (df + math.ceil((time-dt)/ut) * uf if time>dt else df)
    return total_fee
    
    
def solution(fees, records):
    dic = dict()
    for i in range(len(records)):
        time, num, state = records[i].split()
        try:
            dic[num].append([t2m(time),state])
        except:
            dic[num] = [[t2m(time),state]]
    dic_list = sorted(dic.items(), key=lambda x:x[0])
    answer=[]
    for d in dic_list:
        time = 0
        for t in dic[d[0]]:
            t1, state = t
            if(state == "IN"):
                time -= t1
            elif(state == "OUT"):
                time += t1
        if(dic[d[0]][-1][-1] == "IN"):
            time += t2m("23:59")
        f = fee(time, fees)
        answer.append(f)
    return answer                
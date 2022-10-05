
def translate(n, num):
    import string
    str_list = string.digits + string.ascii_uppercase
    q,r = divmod(num,n)
    return translate(n,q) + str_list[r] if q!=0 else str_list[r] 
    
def solution(n, t, m, p):
    from collections import deque
    answer = ""
    idx=0
    history = deque()
    for idx in range(m*t):
        if(len(history) >= m*t):
            break
        temp = deque(list(str(translate(n, idx))))
        while temp:
            te = temp.popleft()
            history.append(te)
    # print(history)
    
    answer=""
    # print(history)
    for idx in range(len(history)):
        if(len(answer) >= t):
            break
        history.rotate(-(p-1))
        answer += history[0]
        history.rotate(-(m-(p-1)))
        
        
    return answer
# test = solution(2,6,2,1)